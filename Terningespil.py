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
            PrintPoint(AntalPoint)
            Igang=False
            break
        
        else:
            AntalPoint += Slag
            PrintPoint(AntalPoint)

            while True:
                count = input("Vil du fortsætte (j/n): ").lower()
                if count in ('j','n'):
                    break
                else:
                    print('WHAT??????????????')
            if count=='n':
                Igang=False
                break

    print("Du fik",AntalPoint,"i denne omgang")
    return AntalPoint


def PrintPoint(AntalPoint):
    print("Du har ialt",AntalPoint)
    print("------------------")