#import RPi.GPIO as GPIO
#GPIO.cleanup()
import hw as hw
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
                hw.beepaj(0.1)
                return karta

def main():
    camera.start()
    hw.priredi_pinove();
    # ucitaj karte
    #for i in range(8):
        #hw.baci_kartu(i)

    hw.beepaj(0.5)
    time.sleep(0.1)
    hw.beepaj(0.1)

    hw.napisi("pocetak igre", 1)
    hw.napisi("Skenirano karata:", 2)
    hw.napisi("0", 3)

    moje_karte = []
    for i in range(6):
        moje_karte.append(skeniraj_novu_kartu())
        hw.napisi(str(i), 3)

    # proslijedi u belai
    for i in range(6):
        print(ime_karte(moje_karte[i]))
    print(0) # robot je uvijek prvi
    print('n') # adut nije izabran

    hw.clearlcd()
    hw.napisi("biranje aduta", 1)

    adut = 'T'
    adutin = input()
    if adutin == "dalje":
        hw.napisi("dalje", 2)
        adut = boje[aduti.zovi(aduti.gledaj())]
        print(adut)
        hw.napisi("adut: " + adut, 4)
    else:
        adut = boje.index(adutin)
        aduti.zovi(adut)
        hw.napisi("adut: " + adutin, 4)

    hw.napisi("skeniraj talon", 1)
    for i in range(6, 8):
        hw.napisi("skenirano: " + str(i-6) + "/2", 2)
        moje_karte.append(skeniraj_novu_kartu())
        print(ime_karte(moje_karte[i]))

    # zvanja
    for i in range(3): print('n')

    time.sleep(2)

    hw.napisi("igra", 1)

    for i in range(32):
        inp = input()
        if len(inp) == 1: # trazi kartu
            hw.napisi("cekam kartu", 2)
            print(ime_karte(skeniraj_novu_kartu()))
        elif inp == "auzmes":
            # zovi auzmes
            hw.napisi("auzmes", 3)
            for i in range(3):
                hw.beepaj(0.5)
                time.sleep(0.3)
            return
        else:
            hw.napisi("bacam kartu", 2)
            bacena_karta = moje_karte.index(karta_imena[inp])
            if i%4 == 0:#ako je robot prvi na redu
                hw.cekaj_gumb()
            hw.baci_kartu(bacena_karta)

    hw.clearlcd()
    hw.napisi(input(), 1)
    hw.odpriredi_pinove()

#GPIO.cleanup()

main()
