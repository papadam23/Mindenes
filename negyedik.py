from turtle import pen


def elso():
    for i in range(51):
        print(i)


    for i in range(182,213):
        print(i)
    
    for i in range(100,201,2):
        print(i)
    
    for i in range(89,56,-2):
        print(i)

    for i in range(1,21):
        print(i,i**2)

    for i in range(99,0,-3):  
        print(i)

    for i in range(101,49,-1):  
        if i%5==0:  
            print(i*2) 
    
    for i in range(1,1000):
        print(i, end=",")
    print("1000.")

    for i in range(1000,0,-3):
        print(i)
    

      
   
def masodik():
    for i in range(100):
        print("*", end="")


    szam=   int (input("Kérek egy egész számot!"))
    szam1=(input("Kérek egy karaktert!"))   
    for i in range(szam):
        print(szam1)

    szoveg= (input("Kérek egy szöveget!"))
    for i in range(len(szoveg)+4):
        print("*",end="")
    print("")    
    print("*",szoveg,"*" )
    for i in range(len(szoveg)+4):
        print("*",end="")
    print("")
        
    print("--------------",)
    for i in range(4):
        print("|", end="")
        for i in range(4):
         
           print("*", " ",end="")
        print("|")
        print("|", end="")
        for i in range(4):
             print(" ", "*",end="")
        print("|")    
    print("--------------")

def harmadik():
    szam=int (input("Kérek egy egész számot!")) 
    szam1=   int (input("Kérek egy egész számot!"))     
    if szam<szam1 :
        for i in range(szam,szam1+1):
            print(i)
    else:
        for i in range(szam1,szam+1):
            print(i)
    
def negyedik():
    pass


def ötödik():
    pass


def hatodik():
    pass


def hetedik():
    szam=   int (input("Kérek egy egész számot!"))  
    fakt=1
    for i in range(2, szam+1,1):
        fakt=fakt*i
    print(fakt,"!")

def kilencedik():
    szam=   int (input("Kérek egy egész számot!"))
    sum=0
    eppenaktualisparatlanszam=1
    for eppenaktualisparatlanszam in range(eppenaktualisparatlanszam,szam,2):  
        sum=sum+eppenaktualisparatlanszam

    print(sum)

        
        
        

        






def main():
    #elso()
    #masodik()
    #harmadik()
    #negyedik()
    #ötödik()
    #hatodik()
    #hetedik()
    kilencedik()
    
    
main()


