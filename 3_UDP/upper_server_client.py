import socket

BUFFSIZE = 65535

def client(network, port):
    #criando o socket para internet e udp
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = input("Envie uma mensagem :")
    sock.sendto(text.encode('ascii'),(network,port))
    while True:
        data, address = sock.recvfrom(BUFFSIZE)
        if not data:
            break;
        print(data.decode('ascii'))


if __name__ == '__main__':
    client('127.0.0.1',1060)