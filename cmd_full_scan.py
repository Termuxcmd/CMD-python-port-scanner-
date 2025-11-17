#!/usr/bin/env python 
import socket
import sys
from datetime import datetime


terget = input("enter the terget IP address: ")
print("_" * 50)
print("scanning terget: " + terget)
print("time started: " + str (datetime.now()))
print("_" * 50)



try:




    for port in range(1, 101):
        s = socket.socket(socket. AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((terget, port))
        if result == 0:
            print(f"port{port}: open")
        s.close()


except keyboardInterrupt:
    print("\nscan interrupted by user.")
except sockect.gaierror:
    print("\Hostname could not be resolved.  exiting.")
    sys.exit()


except socket.error:
    print("\ncould not be connected to the server. exiting.")
    sys.exit()


    print("scan finished at: " + str (datetime.now()))
