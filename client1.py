import socket
import msvcrt

host = "localhost"

sock = socket.socket()
sock.connect((host, 7000))
print("Client has connected to server")
while True:
    key = ord(msvcrt.getch())
    if key == 119: sock.send("forward".encode())
    elif key == 115: sock.send("backward".encode())
    elif key == 97: sock.send("left".encode())
    elif key == 100: sock.send("right".encode())
    elif key == 49: sock.send("pattern_1".encode())
    elif key == 50: sock.send("pattern_2".encode())
    elif key == 51: sock.send("pattern_3".encode())
    elif key == 27:
        sock.send("quit".encode())
        sock.close()
        break
    if key == 224: #special
        key = ord(msvcrt.getch())
        if key == 72: sock.send("size_inc".encode())
        elif key == 80: sock.send("size_dec".encode())
        elif key == 75: sock.send("l_color".encode())
        elif key == 77: sock.send("r_color".encode())