import socket
import sys
import struct

sock: socket = None


def connect(ip: str = "127.0.0.1", port: int = 26541):
    global sock

    print("Connecting...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((ip, port))
        print("Connected!")
    except ConnectionError:
        print("Unable to connect")
        sys.exit(1)


def setUpdateCallback(cb):
    global updateCallback
    updateCallback = cb


def move(value: tuple[float, float]):
    global sock

    x = bytearray(struct.pack("f", value[0]))
    y = bytearray(struct.pack("f", value[1]))

    data = bytearray(b'\x00')

    data[1:1] = x
    data[5:5] = y

    sock.sendall(data)


def aim(value: tuple[float, float]):
    global sock

    x = bytearray(struct.pack("f", value[0]))
    y = bytearray(struct.pack("f", value[1]))

    data = bytearray(b'\x02')

    data[1:1] = x
    data[5:5] = y

    sock.sendall(data)


def shoot(value: bool):
    global sock

    data = bytearray(b'\x01')
    if value:
        data[1:1] = b'\x01'
    else:
        data[1:1] = b'\x00'

    print(data[1])
    sock.sendall(data)


def raycast() -> float:
    global sock

    data = bytearray(b'\x03')

    sock.sendall(data)

    return struct.unpack('f', sock.recv(4))
