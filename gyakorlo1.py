import math
import random
def elso():

    magassag=int (input("Kérem a 3szög magasságát!")) 
    oldal=   int (input("Kérem az egyik odalt!")) 
    
    if magassag>0 and oldal>0:
        terulet= (oldal*(magassag*oldal))/2
        print("Terület:", terulet)
    else:
        print("Nem jó adatok")

def masodik():
    szam=   int (input("Kérek egy egész számot!"))
    szam2=   int (input("Kérek egy egész számot!"))
    szam3=   int (input("Kérek egy egész számot!"))
    if szam==szam2==szam3:
        print("Lehet, egyenkő oldalú 3szög")
    elif szam==szam2 or szam==szam3 or szam2==szam3:
        print("Lehet, egyenlő szárú 3szög")
    elif szam<0 or szam2<0 or szam3<0:
        print("Nem lehet")
    else:
        print("Álatlános 3 szög")

def harmadik():
    szam=   int (input("Kérek egy egész számot!"))
    szam2=   int (input("Kérek egy egész számot!"))
    szam3=   int (input("Kérek egy egész számot!"))
    if szam==szam2 or szam==szam3 or szam2==szam3:
        print("Egyenlő szárú 3szög")
    else:
        print("Nem az ")

def negyedik():
    fizetes=   int (input("Kérem a fizetését "))
    beosztás=input("Kérem a beosztását")
    if beosztás=="vezető":
        ujfizetes= (fizetes*0.25)+fizetes
        print("Az új fizeteése:", ujfizetes)
    else:
        ujfizetes= (fizetes*0.15)+fizetes
        print("Az új fizeteése:", ujfizetes)

def ötödik():
    fizetes=   int (input("Kérem a fizetését "))
    beosztás=input("Kérem a beosztását")
    while beosztás!="":
        if beosztás=="vezető":
            ujfizetes= (fizetes*0.25)+fizetes
            print("Az új fizeteése:", ujfizetes)
            
        
        else:
            ujfizetes= (fizetes*0.15)+fizetes
            print("Az új fizeteése:", ujfizetes)
        beosztás=input("Kérem a beosztását")

def hatodik():
    szam=   int (input("Kérek egy egész számot!"))    
    for i in range(szam,0,-1):
        print(szam) 
        szam=szam-1

def hetedik():
    szam=   int (input("Kérek egy egész számot!"))   
    if szam>0: 
        for i in range(szam,0,-1):
            print(szam) 
            szam=szam-1
    else:
        print("Nem jó szám!")

def nyolcadik():
    szam=   int (input("Kérek egy egész számot!"))   
    while True:
        if szam>0:
            print(szam) 
            szam=szam-1
        elif szam<0:
            print("Nem jó szám!")
            szam=   int (input("Kérek egy egész számot!"))

def kilencedik():
    szam=   int (input("Kérek egy egész számot!"))
    szam2=   int (input("Kérek egy egész számot!"))
    if szam<szam2:
        for i in range(szam,szam2+1):
            print(math.sqrt(szam))
            szam=szam+1
    elif szam>szam2:
       for i in range(szam2,szam+1):
            print(math.sqrt(szam2))
            szam2=szam2+1
def tizedik():
    szam=   int (input("Kérek egy egész számot!"))
    fakt=1
    for i in range(szam-1):
        faktszam=szam*fakt
        fakt=fakt+1
        szam=faktszam
    print("A faktoriális:",faktszam)

def tizedik2():
    szam=   int (input("Kérek egy egész számot!"))
    fakt=1
    szam2=szam
    while fakt!=szam2:
        faktszam=szam*fakt
        fakt=fakt+1
        szam=faktszam
    print("A faktoriális:",faktszam)            
    
def tizedik3():
    szam=   int (input("Kérek egy egész számot!"))
    szam2=1
    faktszam=1
    while True:
        if szam2!=szam+1:
            faktszam= faktszam*szam2
            szam2+=1 
        else:
            break
    print("A faktoriális:",faktszam) 

def tizenegy():
    n=int (input("Kérek egy egész számot!"))  
    db=0  
    for i in range(n):
        szam= random.randint(1,3)
        print(szam)
        if szam==2:
            db=db+1
            print("ennyi van belőle",db)  
    
        
             

                   
    
        
    
            
     
        
            
            
                    
          
          
           
        
    
    



def main():
    #elso()
    #masodik()
    #harmadik()
    #negyedik()
    #ötödik()
    #hatodik()
    #hetedik()
    #nyolcadik()
    #kilencedik()
    #tizedik()
    #tizedik2()
    #tizedik3()
    tizenegy()

main()

