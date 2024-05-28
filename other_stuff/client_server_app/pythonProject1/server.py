import socket
import threading

def handle_client(client_socket):
    try:
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {message}")
        response = "hello"
        client_socket.send(response.encode('utf-8'))
    finally:
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Server listening on port 9999")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()

