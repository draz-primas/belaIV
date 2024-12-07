import RPi.GPIO as GPIO
import time

beeppin = 8
pinovi = [32, 31, 33, 36, 35, 37, 38, 40]
pwm = []
gumb_cekaj_pin = 12
#          B   G   Y   R
lampice = [11, 13, 15, 16]

def priredi_pinove():
    GPIO.setmode(GPIO.BOARD)
    for pin in pinovi:
        GPIO.setup(pin, GPIO.OUT)
        pwm.append(GPIO.PWM(pin, 50))
    for i in range(8):
        pwm[i].start(0)

    GPIO.setup(beeppin, GPIO.OUT)
    GPIO.setup(gumb_cekaj_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def odpriredi_pinove():
    for i in range(8):
        pwm[i].stop()
    GPIO.cleanup()
    pwm = []

def baci_kartu(n):
    pwm[n].ChangeDutyCycle(5)
    time.sleep(2)
    pwm[n].ChangeDutyCycle(9)
    time.sleep(2)
    pwm[n].ChangeDutyCycle(0)


def beepaj(sekundi):
    GPIO.output(beeppin, GPIO.HIGH)
    time.sleep(sekundi)
    GPIO.output(beeppin, GPIO.LOW)

def smije_bacit():
    return GPIO.input(gumb_cekaj_pin)

def cekaj_gumb():
    for i in range(4):
        beepaj(0.1)
        time.sleep(0.1)
    beepaj(0.5)
    while not smije_bacit():
        time.sleep(0.2)


