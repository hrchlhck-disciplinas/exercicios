import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as fd:
    fd.connect(('localhost', 8888))

    while True:
        try:
            msg = str(input('>>> ')).encode('utf8')

            # Implemente um algoritmo de criptografia simétrica a partir daqui

            fd.send(msg)
            recv_msg = fd.recv(1024).decode()

            print('Received:', recv_msg)
        except KeyboardInterrupt:
            fd.send('exit'.encode('utf8'))
            break