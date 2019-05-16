import RPi.GPIO as GPIO
from time import sleep
from random import randint

GPIO.setmode(GPIO.BCM)

R = 18
G = 19
B = 20

GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

for n in range(25):
    i = randint(0,6)
    if(i == 0): # Red
        GPIO.output(R, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(R, GPIO.LOW)
        sleep(0.1)
    if(i == 1): # Green
        GPIO.output(G, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(G, GPIO.LOW)
        sleep(0.1)
    if(i == 2): # Blue
        GPIO.output(B, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(B, GPIO.LOW)
        sleep(0.1)
    if(i == 3): # Yellow
        GPIO.output(R, GPIO.HIGH)
        GPIO.output(G, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(R, GPIO.LOW)
        GPIO.output(G, GPIO.LOW)
        sleep(0.1)
    if(i == 4): # Purple
        GPIO.output(R, GPIO.HIGH)
        GPIO.output(B, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(R, GPIO.LOW)
        GPIO.output(B, GPIO.LOW)
        sleep(0.1)
    if(i == 5): # Cyan
        GPIO.output(G, GPIO.HIGH)
        GPIO.output(B, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(G, GPIO.LOW)
        GPIO.output(B, GPIO.LOW)
        sleep(0.1)
    if(i == 6): # White
        GPIO.output(R, GPIO.HIGH)
        GPIO.output(G, GPIO.HIGH)
        GPIO.output(B, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(R, GPIO.LOW)
        GPIO.output(G, GPIO.LOW)
        GPIO.output(B, GPIO.LOW)
        sleep(0.1)

GPIO.cleanup()
