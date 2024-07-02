import random

AntalPoint = 0
cnt=''

def Slaa():
    min_vaerdi = 1
    max_vaerdi = 6
    Slaa = random.randint(min_vaerdi, max_vaerdi)
    
    return Slaa

while cnt != 'n' and AntalPoint < 50:
    Slag = Slaa()
    print("Du slog: ",Slag)
    AntalPoint += Slag
    print("Du har ialt",AntalPoint)
    print("------------------")
    cnt = input("Vil du fortsætte (j/n): ").upper()
    if cnt in ('j','n'):
        break
    else:
        print('OK')

print("Du fik i alt:", AntalPoint) 
