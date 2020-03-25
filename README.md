# IT011FP - turtlecontrolv4

Beautiful implementation of Python's turtle using server-client programming 

## Author
* **Joriz Bulauitan**

## How to Setup
On the Windows machine that will be the *"server"*, open the command prompt and type **ipconfig** look for the field **Ethernet adapter Ethernet**, under it should be the IPv4 Address you will use as the address for the **host** variable in both *server1.py* and *client1.py*.

The *"server"* machine will be running the *server1.py* while the *"client"* machine will be responsible for running the *client1.py*

## Getting Started
The program is an implementation of Python's **turtle** on the server controlled by the client using **socket**. The keyboard presses are captured by the **msvcrt** library and translated as *move* commands, which are then encoded and sent to the server. The program also implements three aesthetically pleasing patterns from *https://www.geeksforgeeks.org/turtle-programming-python/*.

The responsibilities of *server1.py* is first, generating the screen from the **turtle** library, creating and opening the server using **socket**, defines functions to simplify the manipulation of received commands, and finally, enters a *while* loop to run all the pieces together.

On the other hand, *client1.py* has a simple interface, it connects to the server and waits for keyboard presses using **msvcrt**, if a keyboard press is captured and found valid, it translates it into a *move* command and send it into the server to manipulate the turtle.