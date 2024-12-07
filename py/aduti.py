from RPi import GPIO
import time
import hardware

#         T   K   H   P
pinovi = [11, 15, 16, 13]#B:11 G:13 Y:15 R:16
GPIO.setmode(GPIO.BOARD)
for pin in pinovi:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

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
        time.sleep(0.5)
        hardware.beepaj(0.1)
    return stisnut_gumb

def zovi(adut):
    for pin in pinovi:
        GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pinovi[adut], GPIO.HIGH)
    return adut

def ugasi():
    for pin in pinovi:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

