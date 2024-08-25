import socket

host = "127.0.0.1"
port = 90


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        s.connect((host, port))
        print(f'connected tp {host} on {port}')

        while True:
            cont = input('Client:')
            s.send(cont.encode())
            if cont == 'close':
                s.close()
                print("terminated connecttion")
                break
            response = s.recv(4096).decode()
            print(f'server: {response}')
    except Exception as e:
        print(f'error {e}')
    finally:
        s.close()
        print("disconnected from server")


connect()
