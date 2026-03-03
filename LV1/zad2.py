# Zadatak 1.4.2 Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja
# nekakvu ocjenu i nalazi se izme ¯ du 0.0 i 1.0. Ispišite kojoj kategoriji pripada ocjena na temelju
# sljede´cih uvjeta:
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe).
# Takod¯er, ako je broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuc´u poruku.

print("")

ocjena = 0
while True:
    try:
        ocjena = float(input("Unesite ocjenu: "))

        if not (ocjena >= 0.0 and ocjena <= 1.0):
            raise IndexError
        
        if ocjena >= 0.9:
            print("A")
        elif ocjena >= 0.8:
            print("B")
        elif ocjena >= 0.7:
            print("C")
        elif ocjena >= 0.6:
            print("D")
        else:
            print("F")
        
        break
    except ValueError:
        print("Pogreška pri unosu. Pokušajte ponovno.")
    except IndexError:
        print("Ocjena mora biti u rasponu 0.0 do 1.0!")