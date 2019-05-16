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
    if(i == 0):
        GPIO.output(R, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(R, GPIO.LOW)
        sleep(0.1)
    if(i == 1):
        GPIO.output(G, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(G, GPIO.LOW)
        sleep(0.1)
    if(i == 2):
        GPIO.output(B, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(B, GPIO.LOW)
        sleep(0.1)
    if(i == 3):
        GPIO.output(R, GPIO.HIGH)
        GPIO.output(G, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(R, GPIO.LOW)
        GPIO.output(G, GPIO.LOW)
        sleep(0.1)
    if(i == 4):
        GPIO.output(R, GPIO.HIGH)
        GPIO.output(B, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(R, GPIO.LOW)
        GPIO.output(B, GPIO.LOW)
        sleep(0.1)
    if(i == 5):
        GPIO.output(G, GPIO.HIGH)
        GPIO.output(B, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(G, GPIO.LOW)
        GPIO.output(B, GPIO.LOW)
        sleep(0.1)
    if(i == 6):
        GPIO.output(R, GPIO.HIGH)
        GPIO.output(G, GPIO.HIGH)
        GPIO.output(B, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(R, GPIO.LOW)
        GPIO.output(G, GPIO.LOW)
        GPIO.output(B, GPIO.LOW)
        sleep(0.1)

GPIO.cleanup()
