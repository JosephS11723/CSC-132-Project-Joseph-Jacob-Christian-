import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

S = 24

GPIO.setup(S, GPIO.OUT)

# 0.001 for counter clockwise - 4 loops - 0.001
# 0.005 for clockwise - 7 loops - 0.005
for n in range(7):
    sleep(1)
    GPIO.output(S, GPIO.HIGH)
    sleep(0.005)
    GPIO.output(S, GPIO.LOW)
    sleep(0.005)

GPIO.cleanup()
