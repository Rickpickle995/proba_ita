# #         0        1   2      3
# osoba = ["Sofija", 20, "plava", True]
# print(osoba)

# print(osoba[1])
# print("Godine:", osoba[1])

# automobili = ["Opel", "Mercedes", "BMW"]
# print(automobili[1])

# for x in range(5,10,2):
#     print(x)
#        #012345
# kurs = "python"
# print(kurs[0])
# print(kurs[1])
# print(kurs[2])
# print(kurs[3])

# #len(sekvenca)
# duzina = len(kurs)

# for x in range(len(kurs)):
#     print("Na poziciji:", x, kurs[x])

# ustanova = "IT Academy"

# for indeks in range(len(ustanova)):
#     print(ustanova[indeks])


'''
0, 1, 2, 3, 4, 5
python
["sofija", 25, True]
    for x in sekvenca:
        
        
'''

primer = "zadatak1"  #for petljom ispisati slovo po slovo pomocu indeksa i range
for indeks in range(len(primer)):
    print(primer[indeks])
    
    
broj_karaktera = len(primer)
print(broj_karaktera)
indeks = 0

while indeks < len(primer):
    print(primer[indeks])
    indeks += 1
    
name = "David car"
name_valid = name.upper()
print(name_valid)

korisnicko_ime = "admin"
uneto_kor_ime = input("Unesi korisnicko ime:")

if korisnicko_ime == uneto_kor_ime.lower():
    print("Dobrodosli!")
else:
    print("Pogresni podaci")
    
racunar = "laptop"
model = "macbook"
racunar + model 
racunar = "desktop"

