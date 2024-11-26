import hardware
import camera

boje = ['T', 'K', 'H', 'P']
znakovi = ['7', '8', '9', 'X', 'J', 'Q', 'K', 'A']

def ime_karte(karta):
    return boje[karta//4] + znakovi[karta%8]

karta_imena = {ime_karte(i) : i for i in range(32)}


vec_skenirane = []

def skeniraj_novu_kartu():
    while True:
        kodovi = camera.get_codes(1)
        for kod in kodovi:
            karta = int(kod.data)
            if karta not in vec_skenirane:
                vec_skenirane.append(karta)
                hardware.beepaj(0.2)
                return karta

def main():
    # ucitaj karte
    moje_karte = [skeniraj_novu_kartu() for i in range(8)]

    # proslijedi u belai
    for i in range(6):
        print(ime_karte(moje_karte[i]))
    print(0) # robot je uvijek prvi
    print('y') # adut je izabran

    # @TODO nabavi aduta
    adut = 0
    print(boje[adut])

    for i in range(6, 8):
        print(ime_karte(moje_karte[i]))

    # zvanja
    for i in range(3): print('n')

    for i in range(32):
        inp = input()
        if len(inp) == 1: # trazi kartu
            print(ime_karte(skeniraj_novu_kartu()))
        elif inp == "auzmes":
            # zovi auzmes
            pass
        else:
            bacena_karta = karta_imena[inp]
            hardware.baci_kartu(bacena_karta)

