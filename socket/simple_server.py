import socket


HOST, PORT = '', 9001

listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_sock.bind((HOST, PORT))
listen_sock.listen(1)

while True:
    client_connection, client_address = listen_sock.accept()
    print(f'Connect with {client_address}')
    request = client_connection.recv(1024)
    print(request)

    http_response = b"""\
HTTP/1.1 200 OK

<p>Hello, World</p>"""

    client_connection.sendall(http_response)
    client_connection.close()
