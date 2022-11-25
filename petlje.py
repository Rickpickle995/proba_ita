# x                                            cilj
# pozicija_automobila = 0
# pozicija_cilja = 10

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# for ime in ["marko", "milos", "marija", "ana", "sofija"]:
#     print("Hello", ime)
    
# print("Prva sledeca linija...")

# for broj in [1, 2, 3, 4, 5]:
#     print("Ovo je broj: ", broj)
    

# for broj in range(5, 10, 2):
#     print("Stampanje broja:", broj)
    
# for broj in range (100, 0, -1):
#     print("Prikaz", broj)
    
# pozicija_automobila = 0
# pozicija_cilja = 10
# # 0, 1, 2 .... 10
# for trenutna_pozicija in range(pozicija_cilja +1):
#     pozicija_automobila = trenutna_pozicija
#     print(pozicija_automobila == pozicija_cilja)
    

# startDate = 2010 
# endDate = 2020
# for godina in range(2021, 2010, -1):
#     print("Godina: ", godina)
    
# for zvizda in range(100):
#     print("*", end="")
    
# print("1\t2\t3\t") # \t napravi tab(razmak)

            #1, 2, 3, 4, 5, 
# zeljeni_broj = int(input("Unesite broj: "))

# for brojac in range(1, zeljeni_broj + 1):
#     print(brojac * 1, end="\t")
#     print(brojac * 2,end="\t")
#     print(brojac * 3, end="\n")

# for x in range(5):               #0 1 2 3 4 petlja u petlji primer
#     for y in range(3):           #0 1 2
#         print("Ovo je X: ", x, "Ovo je Y: ", y)
        
# '''
# #   #   #   #   # 
# #   #   #   #   # 
# #   #   #   #   # 
# #   #   #   #   # 
# #   #   #   #   # 
# '''
# for x in range(6):
#     for y in range(6):
#         print("*", end=" ")
#     print()                 #CRTA 5 ZVEZDICA,NAKON TOGA PRINTUJE NOVI RED I KUCA OPET 5 ZVEZDICA OD 0-5
        
# #* # # # # 
# # *# # # #
# # # *# # # 
# # # # *# #

# for x in range(6):
#     for y in range(6):
#         if x == y:
#             print("*", end=" ")                #
#         else:
#             print("#", end=" ")
#             #print("*" if x == y else "#", end=" ")
#     print()
    


# simbol = "*" if x == y else "#"
for x in range(10):
    for y in range(10):
        if x == 0 or x == 9 or y == 0 or y == 9:
            print("#", end= " ")
        else:
            print(" ", end= " ")
        print()
            
            
    
                
    