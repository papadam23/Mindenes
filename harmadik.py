#elágazások
from cmath import sqrt
import math
"""
if feltétel:
    utasítás
else:
    utasítás


egesz=int (input("Kérek egy egész számot!"))
if egesz < 0:
    print("a megadott szám negatív")
    print ("A szám abszolútértéke ", (-1*egesz))
elif egesz ==0:
    print("a szám nulla")
else :
    print("A megadott szám pozitív", )
    print("A szám absazolútértéke", egesz)
    


szam=int (input("Kérek egy egész számot!"))
a=szam%10
if a/10==0:
    print("Osztható 10-el")
else :
    print(a)


szam=int (input("Kérek egy egész számot , számlálót!"))
nevezo=int (input("Kérek egy egész számot!"))
if nevezo==0:
    print("Hiba, a szám nevezője vagy számlálója nem lehet 0!")

szam=int(input("Kérek egy háromjegyű  pozitív egész számot!"))
a= szam//100
b= szam-(a*100)
tiz=b//10
c=szam-(tiz*10)
egy= c//1
d=szam-(egy*1)

print((a*a*a)+(tiz*tiz*tiz)+(egy*egy*egy)+(d*d*d))


szam=int (input("Kérek egy egész számot!"))
if szam==4:
    print("ez a szám a 4-es")
if szam<10:
    print("a szám kisebb mint 10")
if szam%2==0:
    print("A szám páros")    
if szam>0 and szam<10:
    print("a szám 0 és 10 között van")
if szam%3==0 and szam%5==0:
    print("a szám osztható 3 al és öttel")
if not (szam> 10 and szam< 20):
    print("nem 10 és 20 között van ")

szam=int (input("Kérek egy egész számot!"))
szam1=int (input("Kérek egy egész számot!"))
if szam-szam1==0:
    print("a két szám egynelő")
if  (szam%2==1 and szam1%2==1):
    print("mindkettő páratlan")
if szam%3==0 or szam1%3==0:
    print("legalább az egyik szám osztható 3-al")
if szam<0 and szam1<0:
    print("mindkettő negatív")
if szam<0 and szam1>0:
    print("egyik negatív másik pozitív")

szam=int (input("Kérek a téglalap adatait!"))
szam1=int (input("Kérek a téglalap adatait!"))
if szam==szam1:
    print("ez négyzet")
else:
    print("ez egy téglalap")


szam=   int (input("Kérek egy egész számot!"))  
szam2=   int (input("Kérek egy egész számot!"))  
szam3=   int (input("Kérek egy egész számot!"))  
if szam==szam2==szam3:
    print("egy egy szabályos 3szög")


szam=int (input("Kérek egy egész számot!"))
if szam==10 or szam==100 or szam==1000:
    print("igen")
else:
    print("nem")

szam=int (input("Kérek egy egész számot!"))
if szam>0 and szam<9:
    print("benne van ")
else:
    print("nincs benne ")

szam=int (input("Kérek egy egész számot!")) 
if szam<0 and szam%2==1:
    print("ez egy negatív páratlan szám,")
else:
    print("ez nem negatív páratlan")

szam=int (input("Kérek egy egész számot!")) 
szam2=   int (input("Kérek egy egész számot!"))        
if szam2%szam==0 :
    print("igen az osztója")


szam=   int (input("Kérek egy egész számot!"))  
if szam<0 :
    print(sqrt(szam))
else:
    print("a szám nem negatív")

"""
szam=   int (input("Kérek egy egész számot!"))
szam1=   int (input("Kérek egy egész számot!"))
szam2=   int (input("Kérek egy egész számot!"))
if szam<0 and szam1<0 and  szam2<0 :
    print("Ez egy szabályos 3szög  " ,szam+szam1+szam2)
if szam==szam2 or szam==szam1 or szam2==szam1 or szam==szam1==szam2:
    print("Kerülete", szam+szam1+szam2)
if szam<0 or szam1<0 or  szam2<0 :

    print("Ez nem helyes 3szög")

 

















