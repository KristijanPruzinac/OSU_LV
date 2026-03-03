# Zadatak 1.4.3 Napišite program koji od korisnika zahtijeva unos brojeva u beskonaˇcnoj petlji
# sve dok korisnik ne upiše „Done“ (bez navodnika). Pri tome brojeve spremajte u listu. Nakon toga
# potrebno je ispisati koliko brojeva je korisnik unio, njihovu srednju, minimalnu i maksimalnu
# vrijednost. Sortirajte listu i ispišite je na ekran. Dodatno: osigurajte program od pogrešnog unosa
# (npr. slovo umjesto brojke) na naˇcin da program zanemari taj unos i ispiše odgovaraju´cu poruku.
print("")

numbers = []

while True:
    number = input("Unesite broj: ")

    if number.lower() == "done":
        break
    
    try:
        number = float(number)
        numbers.append(number)
    except ValueError:
        print("Pogrešan unos. Pokušajte ponovno.")

if (len(numbers) == 0):
    print("Niste unijeli nijedan broj!")
else:
    print("Avg: {}, Min: {}, Max: {}".format(sum(numbers) / len(numbers), min(numbers), max(numbers)))
    print(sorted(numbers))