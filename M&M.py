import random
import time
#vraag
hvlMM = int(input("hoeveel kleuren MM's moet er worden toegevoegd aan de zak?"))
            
#kleuren
KleurMM = ["oranje", "blauw", "groen", "bruin"]

#waarde
oranje = 0
blauw = 0
groen = 0
bruin = 0

def MMzakje(Aantal):
    global oranje
    global blauw
    global groen
    global bruin
    mm = 1
    while mm <= Aantal:
        MMrandom = random.choice(KleurMM)
        if  MMrandom == "oranje":
            oranje += 1
        elif MMrandom == "blauw":
            blauw += 1
        elif MMrandom == "groen": 
            groen += 1 
        elif MMrandom == "bruin":
            bruin += 1
        mm += 1
    print("Inhoud van de zak:")
    time.sleep(2)
    print(" oranje", str(oranje), "\n blauw", str(blauw), "\n groen: ", str(groen), "\n bruin", str(bruin))
MMzakje(hvlMM)