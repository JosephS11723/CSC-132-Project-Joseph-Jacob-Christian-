import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Functions(object):
    
    def __init__(self):
        # Sets up the MFRC522 RFID Module
        self.reader = SimpleMFRC522()
        
    # Writes the RFID Tag
    def Write(self, text):
        try:
            # Tells you to place RFID tag near module to write
            print("Now place your tag to write")
            # waits for an RFID card to be nearby to write, will write once it detects a nearby card
            self.reader.write(text)
            print("Written")
        finally:
            # cleans up the GPIO pins
            GPIO.cleanup()
            
    # Reads the RFID Tag
    def Read(self):
        try:
            # reads the RFID card returning the serial ID and any text written to the card
            id, text = self.reader.read()
            # returns the serial id and text of the card
            return id, text
        finally:
            # cleans up the GPIO pins
            GPIO.cleanup()
