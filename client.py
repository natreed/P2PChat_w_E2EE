# Copyright (C) 2015 Nathan Reed, natreed@pdx.edu.  Created in collaboration
# with Rachael Johnson arenjae.com, email: rj@arenjae.com
# Also in close collaboration with the CS300 class and Bart Massey, Professor

import socket

def clientFunc(target, message):
    try:
        print("Connecting on {}:{}.".format(*target))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect(target)
        sock.send(message)

    except KeyboardInterrupt:
        print("Killed.")
    finally:
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
