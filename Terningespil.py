# Dette program kører terning-spillet for en person. 
# Tager personens navn som indput 
# Returnerer resultatet af runden når brugeren vvælger at stoppe, eller 0 hvis der slåes en 1'er

import Terning

PointBank=0
AntalPoint = 0
count=''


while count != 'n' and AntalPoint + PointBank < 50:
    Slag = Terning.Slaa(1,6)
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
