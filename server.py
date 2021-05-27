import socket
from datetime import date, datetime


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDP_IP = '127.0.0.1'
    UDP_PORT = 2023
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode('utf-8')
        if data == 'date':
            message = bytes(f'{str(datetime.now().day // 10)}{str(datetime.now().day % 10)}.{str(datetime.now().month // 10)}{str(datetime.now().month % 10)}.{str(datetime.now().year)}', 'utf-8')
        elif data == 'time':
            message = bytes(f'{str(datetime.now().hour // 10)}{str(datetime.now().hour % 10)}' + ':' +
                            f'{str(datetime.now().minute // 10)}{str(datetime.now().minute % 10)}' + ':' +
                            f'{str(datetime.now().second // 10)}{str(datetime.now().second % 10)}' + '.' +
                            f'{str(datetime.now().microsecond)[:3]}',
                            'utf-8')
        elif data == 'datetime':
            message = bytes(f'{str(datetime.now().day // 10)}{str(datetime.now().day % 10)}.{str(datetime.now().month // 10)}{str(datetime.now().month % 10)}.{str(datetime.now().year)}' + ' ' +
                            f'{str(datetime.now().hour // 10)}{str(datetime.now().hour % 10)}' + ':' +
                            f'{str(datetime.now().minute // 10)}{str(datetime.now().minute % 10)}' + ':' +
                            f'{str(datetime.now().second // 10)}{str(datetime.now().second % 10)}' + '.' +
                            f'{str(datetime.now().microsecond)[:3]}',
                            'utf-8')
        else:
            message = bytes('Specified command is not supported', 'utf-8')
        sock.sendto(message, addr)


if __name__ == '__main__':
    main()
