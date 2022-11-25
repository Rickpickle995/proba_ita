osoba = ["Sofija", 25, "plava", False]
                    #4
                    #0 1 2 3 4 
for indeks in range(len(osoba)):
    print(osoba[indeks])
    
                    # "Sofija", 25, "plava", False
    
for osobina in osoba:
    print(osobina)


voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana", "mandarina", "lubenica", "krastavac"]
#0 jabuka
#1 beli luk
#2 crni luk
#3 banana

for stavka in voce_i_povrce:
    print(stavka)
    
for i in range(len(voce_i_povrce)):
    print("Na indeksu:", i, "nalazi se", voce_i_povrce[i])
    
for indeks, vrednost in enumerate(voce_i_povrce):
    print("Indeks:", indeks, "Stavka:", vrednost)
    
             #0           #1     #2...
automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Opel", "Opel"]

# Pozicija 0 Auto: Citroen

for indeks, stavka in enumerate(automobili):
    if len(stavka) == 3:
        print(stavka)
    
    # print("Pozicija", indeks, "Auto", stavka)
    
automobili.append("Mercedes")
automobili[2] = "Opel Corsa"
automobili[3] = "Kia Ceed"
print(automobili)

del automobili[3]
print(automobili)
automobili.remove("BMW")
print(automobili)
automobili.pop(0)
print(automobili)
broj_opela = 0
            # 0 1 2 3 4 5
for indeks in range(len(automobili)):
    if automobili[indeks] == "Opel":
        print("eve ga opel")
        broj_opela += 1
        
print("Imam", broj_opela, "na placu")

automobili.clear()
print(automobili)

prazan_plac = []
#            # 0         #1     #2      #3     #4      #5         #6
automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Peugeot", "Audi"]

automobili_akcija = []

for i in range(len(automobili)):
    if i == 1 or i == 2 or i == 3:
        automobili_akcija.append(automobili[i])
        
print(automobili_akcija)

automobili_akcija = automobili[1:4]             #SLICE precica za prethodni primer  
print(automobili_akcija)



# definisati listu
# prazne liste,prani neparni
# for
# %
#if else

brojevi = [1,2,3,4,5,6,7,8,9,]
parni = []
neparni = []

for broj in brojevi:
    
    if broj % 2 == 0:
        parni.append(broj)
    else:
        neparni.append(broj)
    
print(parni, neparni)

        
    
    

    
