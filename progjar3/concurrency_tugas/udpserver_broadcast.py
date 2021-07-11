import socket
import threading

SERVER_IP = '192.168.122.217'
SERVER_PORT = 5005


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

sock.bind(("", SERVER_PORT))

num = 1

while True:
    data, addr = sock.recvfrom(54272)
    #buffer size 1024 * 53
    print(addr)
    print("diterima ", data)
    print("dikirim oleh " , addr)

    received_image = 'img' + str(num) + ".jpg"
    num += 1
    file = open(received_image, 'wb')
    file.write(data)
    file.close()