"""
Server file
"""


import socket


# SERVER_HOST = "localhost"
SERVER_HOST = "192.168.1.159"
SERVER_PORT = 8888


def main() -> None:

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_HOST, SERVER_PORT))
    server.listen(4)
    print(f"Initializing server at {SERVER_HOST}:{SERVER_PORT}")

    client, client_address = server.accept()
    print(f"Connected to client at {client_address[0]}:{client_address[1]}")

    while True:

        try:
            receive_data = client.recv(1024).decode('utf-8')
            client.send(f"Server Acknowledged.\n".encode('utf-8'))
            # print(f"Received {receive_data} from client.")

            if "CLOSE PORT AND DIE" in receive_data:
                client.close()
                print(f"Server connection closed. Farewell, World.")
                break

            if "FUNC1" in receive_data:
                print(f"Running FUNC1")

        except Exception as e:
            print(f"{e}")
            client.close()
            print(f"Exception. Connection closed.")
            break


if __name__ == "__main__":
    main()
