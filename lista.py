lista=[2,6,4,5,9,7]
print(lista)
print(*lista) #csak a lista elemeit mutatja
print(*lista,sep="; ") #separátorral
print(lista[2]) #3. elem bekérése, print(lista[x]) x-edik elem bekérése
szam=   int (input("Kérek egy egész számot!"))
if szam>len(lista): #len a lista hossza
    print("no")
else:
    print(lista[szam-1])
lista2=[]
print(len(lista2))

lista3=[1,2,"alma",True, 1.2,"körte"] #vegyes lista
sumlist=lista+lista3 #listák összeadása
print(*sumlist)
multilist=lista*3 #lista szorzása
print(*multilist)
print(2 in lista)# benne van e a listába?
if 2 in lista:
    print("A 2 benne van")

print(lista[2:4])# harnadik elemtől az ötödikig
print(lista[2:]) # harmadikk elemtől
print(lista[:3])#negyedik elemig
lista[2]=100 # lista X-ig elemének értékének megváltoztatása
lista.append(500)# a lista végére fűz be elemeket




def feltolt(nevek):
   
    nev= int (input("Hány név van a listában?"))
    for i in range (nev):
        nevek.append(input("Add meg a következő nevet"))

def kiir(listakiir): #létrehozni egy listát
    for item in listakiir: #elemek száma a listába 
        print(item)
neveka=[]
feltolt(neveka)
kiir(neveka)
nevekb=[]
feltolt(nevekb)
nevekc=[]
feltolt(nevekc)     # többször felhasználható a program 



nevekb.insert(2,"Gyula")   #beszúr egy helyre 
nevekb.clear() #lista elemeinek törlése
nevekb.pop(3)#x helyen lévő adat törlése
nevekb.remove("Gyula") # az első elfordulást törli





