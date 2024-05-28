import socket


def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 9999))

        message = input("Enter your message: ")  # Citim mesajul de la tastatura
        client.send(message.encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        client.close()


if __name__ == "__main__":
    main()


