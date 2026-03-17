# Zadatak 3.4.1 Skripta zadatak_1.py ucitava podatkovni skup iz ˇ data_C02_emission.csv.
# Dodajte programski kod u skriptu pomocu kojeg možete odgovoriti na sljede ´ ca pitanja: ´
# a) Koliko mjerenja sadrži DataFrame? Kojeg je tipa svaka velicina? Postoje li izostale ili ˇ
# duplicirane vrijednosti? Obrišite ih ako postoje. Kategoricke veli ˇ cine konvertirajte u tip ˇ
# category.
# b) Koja tri automobila ima najvecu odnosno najmanju gradsku potrošnju? Ispišite u terminal: ´
# ime proizvoda¯ ca, model vozila i kolika je gradska potrošnja. ˇ
# c) Koliko vozila ima velicinu motora izme ˇ du 2.5 i 3.5 L? Kolika je prosje ¯ cna C02 emisija ˇ
# plinova za ova vozila?
# d) Koliko mjerenja se odnosi na vozila proizvoda¯ ca Audi? Kolika je prosje ˇ cna emisija C02 ˇ
# plinova automobila proizvoda¯ ca Audi koji imaju 4 cilindara? ˇ
# e) Koliko je vozila s 4,6,8. . . cilindara? Kolika je prosjecna emisija C02 plinova s obzirom na ˇ
# broj cilindara?
# f) Kolika je prosjecna gradska potrošnja u slu ˇ caju vozila koja koriste dizel, a kolika za vozila ˇ
# koja koriste regularni benzin? Koliko iznose medijalne vrijednosti?
# g) Koje vozilo s 4 cilindra koje koristi dizelski motor ima najvecu gradsku potrošnju goriva? ´
# h) Koliko ima vozila ima rucni tip mjenja ˇ ca (bez obzira na broj brzina)? ˇ
# i) Izracunajte korelaciju izme ˇ du numeri ¯ ckih veli ˇ cina. Komentirajte dobiveni rezultat.

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data_C02_emission.csv")

print("Broj redaka {}".format(data.shape[0]))
print()

columns = data.columns.to_list()
dtypes = data.dtypes.to_list()
for i in range(data.shape[1]):
    print("{}     {}".format(columns[i], dtypes[i]))

data.drop_duplicates("Model", inplace=True)

print()

print("Broj redaka nakon drop {}".format(data.shape[0]))

print()

data.sort_values("Fuel Consumption City (L/100km)", ascending=True, inplace=True)
print("Najmanja gradska potrosnja")
print("Make  Model  Fuel Consumption City (L/100km)")
for i in range(3):
    print("{}  {}  {}".format(data.iloc[i]["Make"], data.iloc[i]["Model"], data.iloc[i]["Fuel Consumption City (L/100km)"]))

print()

data.sort_values("Fuel Consumption City (L/100km)", ascending=False, inplace=True)
print("Najveca gradska potrosnja brrm brrm")
print("Make  Model  Fuel Consumption City (L/100km)")
for i in range(3):
    print("{}  {}  {}".format(data.iloc[i]["Make"], data.iloc[i]["Model"], data.iloc[i]["Fuel Consumption City (L/100km)"]))

vozila_velicina = data.loc[data["Engine Size (L)"] >= 2.5].loc[data["Engine Size (L)"] <= 3.5]
print("{}    Prosjecna emisija {}".format(vozila_velicina, vozila_velicina["CO2 Emissions (g/km)"].mean()))

print("Audi automobila {}".format(len(data[data["Make"] == "Audi"])))
print("Prosjecna emisija audi s 4 cilindra {}".format(data.query("Make == 'Audi' and Cylinders == 4")["CO2 Emissions (g/km)"].mean()))

cetiri = data.query("Cylinders == 4")
sest = data.query("Cylinders == 6")
osam = data.query("Cylinders == 8")
print("Broj vozila {}, Prosjecna emisija vozila s 4 cilindra {}".format(len(cetiri), cetiri["CO2 Emissions (g/km)"].mean()))
print("Broj vozila {}, Prosjecna emisija vozila s 6 cilindra {}".format(len(sest), sest["CO2 Emissions (g/km)"].mean()))
print("Broj vozila {}, Prosjecna emisija vozila s 8 cilindra {}".format(len(osam), osam["CO2 Emissions (g/km)"].mean()))

print("Dizel  Benzin")
print("{}  {}".format(data.query("`Fuel Type` == 'Z'")["CO2 Emissions (g/km)"].mean(), data.query("`Fuel Type` == 'X'")["CO2 Emissions (g/km)"].mean()))
print("{}  {}".format(data.query("`Fuel Type` == 'Z'")["CO2 Emissions (g/km)"].median(), data.query("`Fuel Type` == 'X'")["CO2 Emissions (g/km)"].median()))

print()

bingchilling = data.query("`Fuel Type` == 'Z' and Cylinders == 4").sort_values("Fuel Consumption City (L/100km)", ascending=False)
print("{}".format(bingchilling.iloc[0]))

print("Vozila s rucnim tipom brm brm {}".format(len(data.query("Transmission.str.startswith('AM')"))))

print(data.corr(numeric_only=True))










data["Fuel Consumption City (L/100km)"].plot(kind='hist')

data.plot.scatter(x="Fuel Consumption City (L/100km)", y="CO2 Emissions (g/km)")

data.boxplot(column="Fuel Consumption Hwy (L/100km)", by="Fuel Type")

plt.show()