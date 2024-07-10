# Dette program håndterer logikken omkring hvor mange spillere der er og hvornår spillet stopper
# Det håndterer også hvormange poient hver spilelr har undervejs
# Den kårer en vinder når der er nået 50 poient


import Terningespil
i=0
print("************************************")
print("* Hej - Velkommen til Terningespil *")
print("************************************")

Spillere = []

# Initiering af spillerliste (Kan flyttes ud i en selvstændig fil)
AntalSpillere = int(input("Hvor mange spillere?"))
for i in range(AntalSpillere):
    navn = input(f"Navn på spiller {i+1}?: ")
    Spillere.append([navn, 0]) 
    
# Udskriv listen for at se at den er dannet korrekt
#bemærk at hvert element i listen er både navn og score
print(Spillere)

#Skriv at vi nu starter på runden
print("Runde 1:")

# Spil runde 1 (Mangler at lave en løkke der kører indtil en spiller når max)
for i, Person in enumerate(Spillere):
    Spillere[i][1] = Terningespil.spil()
    print(f"{i+1}. {Person[0]}: {Person[1]}")



# To forskellige måder at udskrive listen på (Den sidste er pænest)

# Nr 1    
print(Spillere)

# Nr 2
for Spiller in Spillere:
    print("Spiller:",Spiller[0],", Point:",Spiller[1])




