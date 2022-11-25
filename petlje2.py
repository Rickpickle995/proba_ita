# for x in range(1, 7): #visina 1,2,3,4,5,6
#     for y in range(5): #sirina 0,1,2,3,4
#         print("#", end="ABCD") # kada odstampa 5 puta # prelazi u novi red kada je end=""
#     print("novi red")


 #########   #<---- ISPISI U KOMANDI
   #######
    ######
     #####
      ####
       ###
        ##
         #

for x in range(10):
    for y in range(10):
        if y > x:
            print("#", end="")
        else:
            print(" ", end="")
    print()
        
automobil = 0
cilj = 100
gorivo = 10
brzina = 10

while automobil < cilj:
    print("Voznja je u toku.")
    automobil += brzina
    gorivo -= 5
    if gorivo == 0:
        break
else:
    print("automboil je stigao na cilj.")
print("U svakom slucaju printic.")