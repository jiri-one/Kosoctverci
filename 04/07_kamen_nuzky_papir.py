from random import randrange
cislo = randrange(3)


if cislo == 0:
    tah_pocitace = "kámen"
   
elif cislo == 1:
    tah_pocitace = "nůžky"
    
else:
    tah_pocitace = "papír"
    
#print(tah_pocitace)

tah_hrace = input("Jaký volíš tah? ")

if tah_hrace == "kámen":
    if tah_pocitace == "kámen":
        print("Remíza")
    elif tah_pocitace == "nůžky":
        print("Vyhrál jsi")
    elif tah_pocitace == "papír":
        print("Prohrál jsi")

elif tah_hrace == "nůžky":
    if tah_pocitace == "kámen":
        print("Prohrál jsi")
    elif tah_pocitace == "nůžky":
        print("Remíza")
    elif tah_pocitace == "papír":
        print("Vyhrál jsi")

elif tah_hrace == "papír":
    if tah_pocitace == "kámen":
        print("Vyhrál jsi")
    elif tah_pocitace == "nůžky":
        print("Prohrál jsi")
    elif tah_pocitace == "papír":
        print("Remíza")

else:
    print ("Promiň, znám jen tahy kámen, nůžky a papír ")
