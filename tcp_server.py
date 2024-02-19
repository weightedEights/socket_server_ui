"""
Server file.
"""


import socket
import funcs


def tcp_server(server_host, server_port):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_host, server_port))
    server.listen(4)
    print(f"Initializing server at {server_host}:{server_port}")

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

            if "func1" in receive_data:
                if not funcs.func1():
                    print(f"func1 failed")

        except Exception as e:
            print(f"{e}")
            client.close()
            print(f"Exception. Connection closed.")
            break
