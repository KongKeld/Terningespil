import random

AntalPoint = 0
count=''

def Slaa():
    min_vaerdi = 1
    max_vaerdi = 6
    Slaa = random.randint(min_vaerdi, max_vaerdi)
    
    return Slaa

while count != 'n' and AntalPoint < 50:
    Slag = Slaa()
    print("Du slog: ",Slag)
    AntalPoint += Slag
    print("Du har ialt",AntalPoint)
    print("------------------")
    count = input("Vil du fortsætte (j/n): ").upper()
    if count in ('j','n'):
        break
    else:
        print('OK')

print("Du fik i alt:", AntalPoint) 
