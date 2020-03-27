import socket
import turtle
import threading

host = "localhost"

""" turtle settings """
speed = 10
rotation = 10
size = 1
size_limit = 10
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
col_pick = 0

""" create turtle screen """
window = turtle.Screen()
window.setup(width=1024, height=768, startx=20, starty=20)
window.colormode(255)
window.bgcolor("black")
graphic = turtle.Turtle()
graphic.shape("turtle")
graphic.color("white")

""" open server """
sock = socket.socket()
sock.bind((host, 7000))
sock.listen()
print("Server is now listening for connections")
conn, addr = sock.accept()
print("Server has received a client")

def change_shape(inc):
    global size
    global size_limit
    global graphic
    if inc == True:
        if size + 1 <= size_limit:
            size = size + 1
            graphic.shapesize(size, size, size)
    else:
        if size - 1 > 0:
            size = size - 1
            graphic.shapesize(size, size, size)


def change_colors(inc):
    global colors
    global col_pick
    global graphic
    if inc == True:
        if col_pick < len(colors) - 1:
            col_pick = col_pick + 1
            graphic.color(colors[col_pick])
    else:
        if col_pick > 0:
            col_pick = col_pick - 1
            graphic.color(colors[col_pick])

def pattern_1():
    """ code derived from: https://www.geeksforgeeks.org/turtle-programming-python/ """
    graphic.speed(2)
    for i in range(360):
        graphic.pencolor(colors[i % len(colors)])
        graphic.width((i / 100) + 1)
        graphic.forward(i)
        graphic.left(59)

def pattern_2():
    """ code derived from: https://www.geeksforgeeks.org/turtle-programming-python/ """
    graphic.speed(0)
    for i in range(127):
        graphic.circle(i * 5)
        graphic.circle(i * -5)
        graphic.left(i)
        j = i
        if j > 51:
            j = 51
        graphic.color(i, i * 2, j * 5)

def pattern_3():
    """ code derived from: https://www.geeksforgeeks.org/turtle-programming-python/ """
    graphic.speed(2)
    for i in range(100):
        graphic.pencolor(colors[i % len(colors)])
        graphic.circle(i * 5)
        graphic.circle(i * -5)
        graphic.left(i)

def exit_app():
    window.bye()
    sock.close()

""" turtle movement """
def turtle_movement():
    while True:
        move = conn.recv(1024).decode()
        print(move)
        if move == "forward": graphic.forward(speed)
        elif move == "backward": graphic.backward(speed)
        elif move == "right": graphic.right(rotation)
        elif move == "left": graphic.left(rotation)
        elif move == "exit": exit_app()
        elif move == "size_inc": change_shape(True)
        elif move == "size_dec": change_shape(False)
        elif move == "r_color": change_colors(True)
        elif move == "l_color": change_colors(False)
        elif move == "pattern_1": pattern_1()
        elif move == "pattern_2": pattern_2()
        elif move == "pattern_3": pattern_3()
        else: exit_app()

thd = threading.Thread(target=turtle_movement, args=(), daemon=True)
thd.start()
window.mainloop()
print("Server closing")