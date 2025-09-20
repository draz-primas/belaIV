# Bela IV

#### Robot koji igra belu

## Dijelovi

- [belai](https://github.com/draz-primas/belai) - umjetna inteligencija
- [stl fajlovi](https://github.com/onaj-koji-jesam/bela-IV) za 3d printane dijelove
- karte - qr kodovi su u data/qrcodes ()

## Upute

#### Na raspberry pi-ju

Ovaj program je namijenjen za pokretanje na raspberry pi 4. Treba se `pokreni.sh`
stavit na autostart. U `raspi-config` treba uključiti neke opcije (zaboravio sam
što sve točno, bitno je samo da radi i2c, kamera i gpio).

#### Sastavljanje

Neka vam https://pinout.xyz/ pomogne. Kameru treba spojiti na mjesto za kameru
(možete koristiti i običnu usb kameru ako promijenite kod u `py/camera.py`).
Na LCD idu i2c pinovi (SDA, SCL), ground i 5V (sva 4 su na pinoutu u drugom i
trećem redu). Zadnjih 5 redova (osim ground) se koriste za pwm servo motore.
Redosljed: 32, 31, 33, 36, 35, 37, 38, 40 (na pinoutu gledate broj pina, a ne
broj GPIO-a). Motor spojen na pin 32 će baciti kartu koja je prva skenirana.
Pinovi 11, 15, 16, 13 se koriste za gumbe i LED lampice koje predstavljaju adute.
Po tom istom redosljedu: tref, karo, herc, pik. Ovo ćemo uskoro maknut jer imamo
lcd. Beeper ide na pin 8. Mi smo dodali promjenjivi otpornik za kontrolu glasnoće
i LED lampicu ako je prostorija glasna pa se beeper slabo čuje. Gumb za restart
ide na pin 8. Na pin 12 ide gumb koji se stisne kad robot treba bacit kartu. Ovo
možete maknuti ako samo stavite otpornik umjesto gumba. Mi smo stavili switch koji
prebacuje iz jednog u drugo, ali najčešće igramo bez gumba. Možete ovaj dio
maknuti u kodu ako vam smeta.  
Mislim da je to sve. Stavljajte otpornike tamo gdje treba iako nije napisano.

### TODO

- [x] prepoznavanje karata
    - [ ] prepoznavanje bez qr kodova (možda u dalekoj budućnosti)
- [x] mehanizam bacanja karata
- [x] unutarnja logika

