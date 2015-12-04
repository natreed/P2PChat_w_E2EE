# Copyright (C) 2015 Nathan Reed, natreed@pdx.edu.
# Collaborated with Rachael Johnson arenjae.com, email: rj@arenjae.com
# Also in close collaboration with the CS300 class and Bart Massey, Professor
# An invaluable resource for this was https://pymotw.com/2/select/, https://pymotw.com/2/threading/
# https://pymotw.com/2/socket/tcp.html#easy-client-connections
# https://pymotw.com/2/socket/index.html

import socket



def clientFunc(target, message):
    try:
        print("Connecting on {}:{}.".format(*target))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        try:
            sock.connect(target)
            sock.send(message)
        except:
            print("\n\n\n{}:{} is unreachable.".format(*target))
            print("HIT THE ENTER KEY TO RETURN TO THE MENU\n")


    except KeyboardInterrupt:
        print("Process aborted")
    finally:
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()

#function used for testing multiple messages sent simultaneously
def repeat(target, message):
    for i in range(10):
        clientFunc(target, message)