import socket

BUFFSIZE = 65535

#criando o socket
def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #definindo o numero de jogadores
    players = 4

    sock.bind((interface, port))

    while True:
        print('Waiting to accept a new connection')
        # Aceita novas conexões
        # A cada nova conexão, um socket ativo (ou connected socket)
        # é criado e retornado na varíável sc
        sc, sockname = sock.accept()
        print('We have accepted a connection from', sockname)
        print('  Socket name:', sc.getsockname())
        print('  Socket peer:', sc.getpeername())

        # Aguardando o cliente enviar os dados
        message = recvall(sc, 16)
        print('  Incoming sixteen-octet message:', repr(message))


