# Dette program håndterer logikken omkring hvor mange spillere der er og hvornår spillet stopper
# Det håndterer også hvormange poient hver spilelr har undervejs
# Den kårer en vinder når der er nået 50 poient


import Terningespil
PointBank=0


print('Hej')
#Terningespil.spil()

PointBank+=Terningespil.spil()

print("Du har",PointBank,"point i banken")


print("Spillet er slut")


