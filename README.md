# What is it
SimpleSocketChat is a basic Python project that demonstrates client-server communication using sockets and threading.*
The server listens for incoming connections, and clients can connect to the server to send and receive messages.This was done to get more comfortable
with network programming with python.more Features will be added overtime as i progress with python

# How to Run
1. Clone the Repository
git clone https://github.com/Fruitpunch44/Simple-Socket-Chat.git
cd SimpleSocketChat

3. Start the Server
Run the following command to start the server:
python3 mrequest1.py
This will start the server, listening for connections on 127.0.0.1 and port 90
you can try connecting with multiple devices

3. Connect a Client
Open another terminal window and run the following command to start the client
python mrequest2.py
You can open multiple terminal windows and run the client script to simulate multiple clients connecting to the server.

4. Communication
From Client to Server: Type a message in the client terminal and press Enter. The message will be sent to the server, which will display it.
From Server to Client: The server can also send messages to the client by typing in the server's terminal.
Closing the Connection: To close the connection, type close in the client terminal. The connection will be terminated, and the client will disconnect from the server.
