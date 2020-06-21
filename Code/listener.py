#UDP listener (TCP WOULD BE BETTER HOWEVER I AM LAZY AND IT DOESN'T NEED TO BE THAT ACCURATE UNTIL I GET A USB WEBCAM
# Whole point of this is using my laptop as a webcam and transfering data because I dont have a webcam 
# ugly code warning (TEMPORARY)

import os
from socket import *
host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

def Process(new, last):
    if new == last:
        pass # dont do anything
    elif (new < last): # if its less than last turn motor in direction unknown?
        pass
    else: # opposite of new < last
        pass
    
print ("STARTING LISTENER")
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print ("Received message: " + data.decode())
    if data.decode() == "exit":
        break
    else:
        Process(data.decode(), last) # sending new and last values so we can compare and give feedback to our motor

    last = data.decode()
    
UDPSock.close()
exit()
