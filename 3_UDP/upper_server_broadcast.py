import socket

BUFFSIZE = 65535


def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('listening for datagrams at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(BUFFSIZE)
        text = data.decode('utf-8')
        text = text.upper()
        sock.sendto(text.encode('utf-8'),address)
        print('O cliente {} falou : {!r}'.format(address,text))


if __name__ == '__main__':
    server("", 1060)
