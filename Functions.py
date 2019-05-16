import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

class Write(object):
    def __init__(self, text):
        try:
            # Tells you to place RFID tag near module to write
            print("Now place your tag to write")
            # waits for an RFID card to be nearby to write, will write once it detects a nearby card
            reader.write(text)
            print("Written")
        finally:
            # cleans up the GPIO pins
            GPIO.cleanup()
            
# Reads the RFID Tag
class Read(object):
    def __init__(self):
        try:
            # reads the RFID card returning the serial ID and any text written to the card
            id, text = reader.read()
            # returns the serial id and text of the card
            self.text = text
            self.id = id
        finally:
            # cleans up the GPIO pins
            GPIO.cleanup()

    def prtTXT(self):
        return self.text

    def prtID(self):
        return self.id
