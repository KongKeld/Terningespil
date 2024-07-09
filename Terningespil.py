# Dette program kører terning-spillet for en person. 
# Tager personens navn som indput 
# Returnerer resultatet af runden når brugeren vvælger at stoppe, eller 0 hvis der slåes en 1'er

import Terning



def spil():
    AntalPoint = 0
    count=''
    Igang=True
    while Igang:
        Slag = Terning.Slaa(1,6)
        print('----------------------')
        print("Du slog: ",Slag)
        
        if Slag == 1:
            AntalPoint=0
            print("Du har ialt",AntalPoint)
            print("------------------")
            Igang=False
            break
        
        else:
            AntalPoint += Slag
            print("Du har ialt",AntalPoint)
            print("------------------")

            if AntalPoint >= 50:
                break
            while True:
                count = input("Vil du fortsætte (j/n): ").lower()
                if count in ('j','n'):
                    break
                else:
                    print('WHAT??????????????')
            if count=='n':
                Igang=False
                break

    return AntalPoint
