import random
def elso():
    szamok=random.randint(0,10)
    print(szamok)
    szamok1=random.randint(10,15)
    print(szamok1)
    szamok2=random.randint(0,100)
    print(szamok2)
    szamok3=random.randint(-100,100)
    print(szamok3)
    tiz=1
    while tiz!=11:
         szamok4=random.randint(0,1)
         print(szamok4)
         tiz=tiz+1
    negy=1
    while negy!=5:
         szamok5=random.randint(-10,30)
         print(szamok5)
         negy=negy+1


def ketto():
    tipp= int (input("Tegye meg tippjeit!"))
    szamok=random.randint(0,1)
    while tipp!=szamok:
        print("Nem talált, próbálkozzon újra (ez egy bíztatás!4)")
        tipp= int (input("Tegye meg tippjeit!"))
    print("Talált")
        
def negyes():
    nulla=0
    szam=   int (input("Kérek egy egész számot!"))
    while nulla!=szam:
        
        szam=   int (input("Kérek egy egész számot!"))
        szam=szam*szam
        print(szam)
        
    print("Látom megtaláltad a 0-át")

def otodik():
    szavak="alma"
    bekér=input("jhhjnkl")
    while bekér!="":
        szavak=szavak+bekér
        print(szavak)
        bekér=input("jhhjnkl")
    print("Ok")



        


    






def main():
    #elso()
    #ketto()
    #negyes()
    otodik()

main()