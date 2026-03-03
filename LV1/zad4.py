# Zadatak 1.4.4 Napišite Python skriptu koja ´ce uˇcitati tekstualnu datoteku naziva song.txt.
# Potrebno je napraviti rjeˇcnik koji kao kljuˇceve koristi sve razliˇcite rijeˇci koje se pojavljuju u
# datoteci, dok su vrijednosti jednake broju puta koliko se svaka rijeˇc (kljuˇc) pojavljuje u datoteci.
# Koliko je rijeˇci koje se pojavljuju samo jednom u datoteci? Ispišite ih.

print("")

rijeci = dict()

count = 0

file = open("song.txt", "r")
for line in file:
    line = line.rstrip()
    for word in line.split():
        if word[0].lower() == 'd':
            count += 1
            print("!!!!!!!!!!!" + word)
        if word in rijeci.keys():
            rijeci[word] += 1
        else:
            rijeci.update({word: 1})

for rijec in rijeci:
    print("{} {}".format(rijec, rijeci[rijec]))

print("Slovo d: {}".format(count))

file.close()