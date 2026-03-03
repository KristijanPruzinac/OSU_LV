# Zadatak 1.4.1 Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je pla´cen
# po radnom satu. Koristite ugra ¯ denu Python metodu input(). Nakon toga izraˇcunajte koliko
# je korisnik zaradio i ispišite na ekran. Na kraju prepravite rješenje na naˇcin da ukupni iznos
# izraˇcunavate u zasebnoj funkciji naziva total_euro.
# Primjer:
# Radni sati: 35 h
# eura/h: 8.5
# Ukupno: 297.5 eura

print("")

def total_euro(radnih_sati, placen_po_satu):
    return radnih_sati * placen_po_satu


try:
    radnih_sati = int(input("Radni sati: "))
except ValueError:
    print("Nevalja unos")
    exit()
    
placen_po_satu = float(input("eura/h: "))

print("Ukupno (eura): {}".format(total_euro(radnih_sati, placen_po_satu)))