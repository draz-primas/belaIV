#import RPi.GPIO as GPIO
#GPIO.cleanup()
import hardware
import camera
import aduti
import time

#aduti.ugasi()

boje = ['T', 'K', 'H', 'P']
znakovi = ['7', '8', '9', 'X', 'J', 'Q', 'K', 'A']

def ime_karte(karta):
    return boje[karta//8] + znakovi[karta%8]

karta_imena = {ime_karte(i) : i for i in range(32)}


vec_skenirane = []

def skeniraj_novu_kartu():
    while True:
        kodovi = camera.get_codes(1)
        for kod in kodovi:
            karta = int(kod.data)
            if karta not in vec_skenirane:
                vec_skenirane.append(karta)
                hardware.beepaj(0.1)
                return karta

def main():
    camera.start()
    hardware.priredi_pinove();
    # ucitaj karte
    #for i in range(8):
        #hardware.baci_kartu(i)
    
    hardware.beepaj(0.5)
    time.sleep(0.1)
    hardware.beepaj(0.1)
    
    moje_karte = [skeniraj_novu_kartu() for i in range(6)]

    # proslijedi u belai
    for i in range(6):
        print(ime_karte(moje_karte[i]))
    print(0) # robot je uvijek prvi
    print('n') # adut nije izabran

    adut = 'T'
    adutin = input()
    if adutin == "dalje":
        adut = boje[aduti.zovi(aduti.gledaj())]
        print(adut)
    else:
        adut = boje.index(adutin)
        aduti.zovi(adut)

    for i in range(6, 8):
        moje_karte.append(skeniraj_novu_kartu())
        print(ime_karte(moje_karte[i]))

    # zvanja
    for i in range(3): print('n')

    time.sleep(2)

    for i in range(32):
        inp = input()
        if len(inp) == 1: # trazi kartu
            print(ime_karte(skeniraj_novu_kartu()))
        elif inp == "auzmes":
            # zovi auzmes
            for i in range(3):
                hardware.beepaj(0.5)
                time.sleep(0.3)
            return
        else:
            bacena_karta = moje_karte.index(karta_imena[inp])
            if i%4 == 0:#ako je robot prvi na redu
                hardware.cekaj_gumb()
            hardware.baci_kartu(bacena_karta)

    hardware.odpriredi_pinove()

#GPIO.cleanup()

main()
