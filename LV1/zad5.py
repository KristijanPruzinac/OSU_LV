# Zadatak 1.4.5 Napišite Python skriptu koja ´ce uˇcitati tekstualnu datoteku naziva SMSSpamCollection.txt
# [1]. Ova datoteka sadrži 5574 SMS poruka pri ˇcemu su neke oznaˇcene kao spam, a neke kao ham.
# Primjer dijela datoteke:
# ham Yup next stop.
# ham Ok lar... Joking wif u oni...
# spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken’s stuff!
# a) Izraˇcunajte koliki je prosjeˇcan broj rijeˇci u SMS porukama koje su tipa ham, a koliko je
# prosjeˇcan broj rijeˇci u porukama koje su tipa spam.
# b) Koliko SMS poruka koje su tipa spam završava uskliˇcnikom ?

print("")

broj_rijeci_ham = 0
broj_rijeci_spam = 0

broj_ham = 0
broj_spam = 0
broj_usklicnika = 0

count_d = 0

file = open("SMSSpamCollection.txt", "r")
for line in file:
    line = line.rstrip()

    words = line.split()
    identifier = words.pop(0)

    for word in words:
        if identifier == "ham":
            broj_rijeci_ham += 1
        elif identifier == "spam":
            broj_rijeci_spam += 1

            if 'd' in word or 'D' in word:
                count_d += 1
        else:
            print("Neispravan unos u datoteci.")
            print(line)
            exit()
    
    if identifier == "ham":
        broj_ham += 1
    elif identifier == "spam":
        broj_spam += 1
        if line[-1] == "!":
            broj_usklicnika += 1

out_ham = 0 if broj_ham == 0 else round(broj_rijeci_ham / broj_ham, 2)
out_spam = 0 if broj_spam == 0 else round(broj_rijeci_spam / broj_spam, 2)
print("Avg ham: {}, Avg spam {}, SMS Spam s usklicnikom: {}".format(out_ham, out_spam, broj_usklicnika))

print(count_d)

file.close()