#1.test.py
#Jean-Sebastien Paul
#
#About:


# Import required modules
import time
import RPi.GPIO as GPIO
import gpiozero
import pygame
import math
from time import sleep
from gpiozero import Motor

#define trues and falses to prevent slip ups from R or java
T=True
F=False
true = True
false = False

#motor stuff
A1in1=12
A1in2=16
A2in1=20
A2in2=21

B1in1=26
B1in2=19
B2in1=13
B2in2=6

A1=Motor(12,16)
A2=Motor(20,21)
B1=Motor(26,19)
B2=Motor(13,6)
Amotors=[A1,A2]
Bmotors=[B1,B2]
motors=[A1,A2,B1,B2]

#ultrasound stuff
GPIO.setmode(GPIO.BCM)
trig=18
echo=24
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(trig, T)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trig, F)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(echo) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(echo) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance


# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# Get ready to print
textPrint = TextPrint()

# -------- Main Program Loop -----------
while T:
    dist=distance()
    print(dist)
    print('dew')
