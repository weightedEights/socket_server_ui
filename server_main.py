"""
Server file
"""


import tcp_server
import threading


# SERVER_HOST = "localhost"
SERVER_HOST = "192.168.1.159"
SERVER_PORT = 8888


def main() -> None:

    threading.Thread(target=tcp_server.tcp_server(SERVER_HOST, SERVER_PORT), daemon=True).start()


if __name__ == "__main__":
    main()
