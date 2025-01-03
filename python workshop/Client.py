import socket
import threading

HEADER = 1024
SERVER = "192.168.1.5"
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def receive_messages():
    while True:
        try:
            message = client.recv(HEADER).decode(FORMAT)
            print(message)
        except:
            print("Connection closed.")
            break

def main():
    # Prompt for username and send it first
    username = input("Enter your username: ")
    send_message(username)  # Send username as the first message

    # Start thread for receiving messages
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    while True:
        messa
        ge = input()
        if message.lower() == "disconnect":
            send_message(DISCONNECT_MSG)
            break
        send_message(message)

if __name__ == "__main__":
    main()
