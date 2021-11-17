import time


#listen van de dagen
alleDagen = ["Maandag", "Dinsdag","Woensdag", "Donderdag","Vrijdag", "Zaterdag","Zondag"]


#print alle dagen en omgekeerd
print("Alle dagen in de week zijn:")
print(alleDagen)
time.sleep(2)
print("Alle werkdagen zijn?")
print(alleDagen[0:5])
time.sleep(2)
print("Alle weekenddagen zijn?")
print(alleDagen[5:])
time.sleep(2)
print("Dagen in de omgekeerde volgorde:")
alleDagen.reverse()
print(alleDagen)
time.sleep(2)
print("Alle werkdagen in de omgekeerde volgorde zijn?")
alleDagen.reverse()
print(alleDagen[0:5])
time.sleep(2)
print("Alle weekenddagen omgekeerd zijn?")
alleDagen.reverse()
print(alleDagen[4:5])