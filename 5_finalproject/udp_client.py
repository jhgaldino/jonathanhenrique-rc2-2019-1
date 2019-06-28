import socket

BUFFSIZE = 65535

def client(network, port):
    #criando o socket para internet e udp
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)