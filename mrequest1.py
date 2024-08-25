import socket
import sys

import threading


def client(cli):
    try:
        while True:
            buffer = sys.stdin.readline().strip()
            print(f'Server: {buffer}')
            cli.send(buffer.encode())
            if buffer == "close":
                break
    except Exception as e:
        print(f'error {e}')
    finally:
        cli.close()
        print("closed clinet connection")


host = "127.0.0.1"
port = 90


def listento():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        s.bind((host, port))
        s.listen(5)
        print(f'listening on {host} : {port}')
        while True:
            client_sock, addr = s.accept()
            print(f'{addr} connected ')

            client_thread = threading.Thread(target=client, args=(client_sock,))
            client_thread.start()
            while True:
                request = client_sock.recv(4096).decode()
                if not request:
                    break
                print(f'client:{request}')

    except Exception as e:
        print(f'error {e}')
    finally:
        s.close()


listento()
