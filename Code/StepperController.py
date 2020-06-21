#!/usr/bin/env python3
# Stepper Test Program
import tkinter as tkinter
import time
import PiMotor

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
        print('welcome to gladOS')
        for i in range(3):
            startup() # only way to get the lights to blink 3 times and wait
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
        
x = stepper()
for i in range(100):
    x.StepPOS()
    x.StepNEG()
    
