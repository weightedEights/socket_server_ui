"""
Server file
"""


import socket


# SERVER_HOST = "localhost"
SERVER_HOST = "192.168.1.159"
SERVER_PORT = 8888


def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_HOST, SERVER_PORT))
    server.listen(4)
    print(f"Initializing server at {SERVER_HOST}:{SERVER_PORT}..")

    client, client_address = server.accept()
    print(f"Connected to client at {client_address}")

    while True:

        receive_data = client.recv(1024).decode('utf-8')
        client.send(f"Server Acknowledged.".encode('utf-8'))
        # print(f"Received {receive_data} from client.")

        if "CLOSE PORT AND DIE" in receive_data:
            client.close()
            print(f"Server connection closed. Farewell, World.")
            break

        if "FUNC1" in receive_data:
            print(f"Running FUNC1")


if __name__ == "__main__":
    main()
