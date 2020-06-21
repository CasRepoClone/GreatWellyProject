#UDP listener (TCP WOULD BE BETTER HOWEVER I AM LAZY AND IT DOESN'T NEED TO BE THAT ACCURATE UNTIL I GET A USB WEBCAM
# Whole point of this is using my laptop as a webcam and transfering data because I dont have a webcam 
# ugly code warning (TEMPORARY)
#!/usr/bin/env python3
# Stepper Test Program
import tkinter as tkinter
import time
import PiMotor    
import os
from socket import *

m1 = PiMotor.Motor('MOTOR1', 1)
m2 = PiMotor.Motor('MOTOR2', 1)
m3 = PiMotor.Motor('MOTOR3', 1)
m4 = PiMotor.Motor('MOTOR4', 1)

ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3)
ar = PiMotor.Arrow(4)



class stepper(): # later add in so we can give the two motors and create the two induvidual objects for movment 
    def __init__(self):
        # NOTE SEGFAULTS SOMETIMES ON STEPPING POS OR NEG SO WHAT WE ARE GOING TO DO IS JUST RUN THEM USING TRY EXCEPT
        print('welcome to THE TERMINATOR or gladOS depending on how this goes or just a hybrid of the both terminadOS')
        for i in range(3):
            self.delay = 0.2 # 0.2 sec delay 
            if i == 2:
                m3.forward(100)
                m3.stop()
                time.sleep(2) # after second flash just make it s it sets the motor up ready to move while knowing where we are starting magnet direction wise
            else:
                pass
            
    def StepPOS(self):
        """Step Positive, first step in sequence"""
        #ccw
        m3.forward(100); time.sleep(self.delay)
        m3.stop()
        m4.reverse(100); time.sleep(self.delay) # required to run StepNEG after this as reversed polarity means it wont jump back
        m4.stop()
    def StepNEG(self):                        
        #ccw
        m3.reverse(100); time.sleep(self.delay)
        m3.stop()
        m4.forward(100); time.sleep(self.delay)
        m4.stop()
        # took about 4 hours just to get the pattern right as well as wiring and voltage
    

host = ""
port = 13000 # el listening port
buf = 1024 # buffer size umm like max size of packet?
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr) # bind listener to localhost on the port

def Process(new, last):
    if new == last:
        pass
    elif (new < last): # if its less than last turn motor in direction unknown?
        x.StepPOS()
        x.StepNEG()
    else: # opposite of new < last
        pass
    
print ("STARTING LISTENER")
last = 0 
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
