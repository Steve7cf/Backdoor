#stephan
import socket


HOST = 'localhost'
PORT = 6767

# create socket
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

while True:
    print(f'[+] Listening on {HOST}:{PORT}')
    client = server.accept()
    print(f'[+] client connected {client[1]}')

    client[0].send('connected'.encode())
    while True:
        cmd = input('>>>')
        client[0].send(cmd.encode())

        if cmd.lower() in ['QUIT', 'quit', 'q', 'x']:
            break

        result = client[0].recv(10240).decode()
        print(result)
    client[0].close()
    cmd = input('Wait for new client y/n: ') or 'y'
    if cmd.lower() in ['n', 'no']:
        break
server.close()

