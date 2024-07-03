import random

PointBank=0
AntalPoint = 0
count=''

def Slaa():
    min_vaerdi = 1
    max_vaerdi = 6
    Slaa = random.randint(min_vaerdi, max_vaerdi)
    
    return Slaa

while count != 'n' and AntalPoint + PointBank < 50:
    Slag = Slaa()
    print("Du slog: ",Slag)
     
    if Slag == 1:
        AntalPoint=0
        print("Du har ialt",AntalPoint)
        print("------------------")
        count = input("Vil du fortsætte (j/n): ").upper()

        if count in ('j','n'):
            break
        else:
            print('OK')

    else:
        AntalPoint += Slag
        print("Du har ialt",AntalPoint)
        print("------------------")

        if AntalPoint >= 50:
            break
        else:
            count = input("Vil du fortsætte (j/n): ").upper()
            if count in ('j','n'):
                break
            else:
                print('OK')

print("Du fik i alt:", AntalPoint + PointBank) 
