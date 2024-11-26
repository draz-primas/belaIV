from RPi import GPIO
import time

buttonpin = 10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def stisnuto():
    return GPIO.input(buttonpin)

while not stisnuto(): time.sleep(1)

