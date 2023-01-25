import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as fd:
    fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    fd.bind(('localhost', 8888))

    fd.listen(1)

    while True:
        print('Waiting for connections')
        conn, addr = fd.accept()

        while True:
            msg = conn.recv(1024)
            msg = msg.decode()

            # Implemente um algoritmo de criptografia simétrica a partir daqui
            print(msg)

            if msg == 'exit':
                print('Connection lost')
                break

            conn.send(msg.upper().encode('utf8'))