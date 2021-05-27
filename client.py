import socket



def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        msg = bytes(input(), 'utf-8')
        client_socket.sendto(msg, ('127.0.0.1', 2023))
        data, addr = client_socket.recvfrom(1024)
        print(data.decode('utf-8'))


if __name__ == '__main__':
    main()