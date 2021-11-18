import random

print("M&M: Hoeveel wilt u in de zak doen? ")
amountMnM = int(input("IK: "))
color = ["oranje", "blauw", "groen", "bruin"]
theBag = {}
# Dit is een dictionary, hij is nu leeg, maar later word het gevuld met 
def mnm(amount): 
    for a in range(amount):
        randomColor = random.choice(color)
        if randomColor in theBag:
# Als een kleur van de list color al in theBag zit dan is de value +1 van de kleur in theBag 
            theBag[randomColor] += 1
        else:
# Als de kleur van de list color niet in theBag zit, dan maakt hij een nieuwe key aan in theBag
            theBag.update({randomColor : 1})
# Met update maakt hij een nieuwe key in de dictionary theBag
    return theBag
print(sorted(mnm(amountMnM).items(), key=lambda kv: kv[1], reverse=True))
# .items zorgt ervoor dat hij de value uit print van de keys, sorted zorgt ervoor dat het op alfabetische volgerde staat
# key=lambda kv: kv[1], reverse=True zorgt ervoor dat hij van groot naar klein uitprint