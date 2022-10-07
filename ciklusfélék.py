import random
#szoveg="aranyalma"
#for betu in szoveg:
    #print(betu)

"""jelszo=input("Kérem a jelszót")

"while feltétel- ha a feltétel teljesül akkoraz utasítás lefut"

oldjelszo="Majom"
jelszo=input("Kérem akkor jelszót")
while oldjelszo !=jelszo:
    
    jelszo=input(" rossz jelszó kérem a jelszót: ")
print("jó a jelszó")

Hátultesztelős ciklus: 
True-ra örökké fut If-fel megnézem hogy teljesül e feltétel. Ha igen break-kel kilépünk
while True:
    utasítás
    if feltétel- kilépési feltétel
        break

while True:
    jelszo=input("Kérem akkor jelszót")
    if jelszo==oldjelszo:
        break
print("jó")



megfelelo=False
while not megfelelo:
    jelszo=input("Kérem akkor jelszót")
    if jelszo==oldjelszo:
        megfelelo=True
print("jó")

"""
gondoltszam= random.randint(1,1000)
tippekszama=1
tipp = int (input("Kérek egy egész számot!"))
while tipp !=gondoltszam:
    if tipp<gondoltszam:
        print("Nagyobb szám")
    else:
        print("Kisebb")
    tipp=int (input("Kérek egy egész számot!"))
    tippekszama+=1
print("Eltaláltad!")
print("Tippjeid száma :",tippekszama)




tippekszama=0
gondoltszam= random.randint(1,1000)
while True:
    tippekszama+=1
    tipp= int (input("Kérek egy egész számot!"))
    if tipp==gondoltszam:
        break
print(f"Eltalálta, Tippek száma: {tippekszama}")