from RPi import GPIO
import time
import hardware

#         B   G   Y   R
pinovi = [11, 13, 15, 16]
GPIO.setmode(GPIO.BOARD)

def stisnuto(s_pin):
    return GPIO.input(s_pin)

def gledaj():
    hardware.beepaj(0.1)
    time.sleep(0.1)
    for pin in pinovi:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    hardware.beepaj(0.1)
    time.sleep(0.1)
    stisnut_gumb = -1
    while stisnut_gumb < 0 or stisnut_gumb > 3:
        hardware.beepaj(0.1)
        time.sleep(0.1)
        for i in range(len(pinovi)):
            if stisnuto(pinovi[i]):
                stisnut_gumb = i
        time.sleep(1)
        hardware.beepaj(0.1)
    return stisnut_gumb

def zovi(adut):
    for pin in pinovi:
        GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pinovi[adut], GPIO.HIGH)
    return

