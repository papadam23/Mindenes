from cmath import sqrt
import math

print("Hello World")
print("Hello\nNagyon jó ez a program\nÜdv a program")
print("*********\n*\t*\n*\t*\n*********")
print("*********\n*\t*\n* Ádám\t*\n*********")


print("A \'whitespace\' vagy  \'white space\' angol szóösszetétel, jelentése fehér tér.\n\n Az informatikában, elsősorban a\n\tszövegszerkesztésben és\n\tprogramozásban\nhasználatos kifejezés.\n\n Alapvetően azokat a karaktereket értjük alatta, amelyek nem láthatóak a szövegben viszont valamilyen egyedi funkcióval bírnak. Nincs elterjedt magyar kifejezés rá.\n\t-- A Wikipédiából, (a szabad enciklopédiából)")
print ("Hello...\n+-----------------------+\nł Hetfo\t\t\tł\n+-----------------------+\t\nł 01\tProgramozas\tł\n+-----------------------+\n+-----------------------+\nł Kedd\t\t\tł\n+-----------------------+\t\nł 01\tHalozat\t\tł\n+-----------------------+")
print("55*10 =",55*10)
print("64-20 =",64-20)
print("12+86 =",12+86)
print("52+24*3 =",52+24*3)
print("(52+24)*3 =",(52+24)*3)
print("12//10 =",12//10)
print("10/4 =",10/4)
print("10/4.0 =",10/4.0)
print("10.0/4 =",10.0/4)
print("10.0/4.0 =",10.0/4.0)

alma=10
print(alma,"\nalma")
print(alma*2)
print(alma-2)
print(alma/2)
print(alma**2)
print(alma%2)
print(alma%3)
print(alma%5)


körte=5
print(körte)
körte=körte+1
print(körte)
körte=körte+5
print(körte)
körte=körte-1
print(körte)
körte=körte-3
print(körte)
körte=körte*4
print(körte)
körte=körte/2
print(körte)
körte=körte%3
print(körte)


a=6
print(a)
print("a valtozo aktuális erteke",a)
a=1922
print(a)
a=a+100
print (a)
a=a-2001
print("En, Ádám", a ,"eves vagyok" )
c=float(5)
print (c)
print(c*2)
c=c+3
print (c)

d=3
print(d*10)
e=c/d
print(e)

barack=50
körte=30
print("barack+körte= 50+30=",barack+körte) 
print ("barack-körte= 50-30=",barack-körte) 
print("barack*körte= 50*30=",barack*körte) 
print("barack/körte= 50/30=",barack/körte) 


a=7
b=1
c=3
print((a-b)*c)
print((a+b)*(2*a*c))
print ((a*3-b*3) /c)
print(2*a*c+4*b)

egesz=10
egesz1=20
print (egesz%egesz1)

valos= float=10
valos1=float=20
print (valos%valos1)


egesz4=11
egesz2=27
print (egesz4%egesz2)


valos= float=150
valos1= float=253

print (valos%valos)


szam=int (input("Kérek egy számot!"))
szam2= int (input("Kérek még egy számot!"))
print("szam\t   =\t" ,szam)
print("szam2\t   =\t" ,szam2)
print("----------------------")
print("szam+szam2 =\t",szam+szam2)
print("szam-szam2 =\t",szam-szam2)
print("szam*szam2 =\t",szam*szam2)
print("szam/szam2 =\t",szam/szam2)
print("szam  ^2   =\t",math.pow(szam,2 ))
print("szam2 ^2   =\t",math.pow(szam2,2 ))
print("szam  ^2   =\t",math.pow(szam,3))
print("szam2 ^3   =\t",math.pow(szam2,3))
print("----------------------------------------------------------------------")


print("Második feladatsor")

ár=int (input("Mennyibe kerül 1 Kg krumpli?") )
mennyiség=int(input("Mennyit szeretnél venni?"))
print("Ennyi pénzt kell hozzak:", mennyiség*ár, "Ft")

fizetés= int (input("Mennyi a fizetése?"))
emelés=int(input("Hány  százalék emelést fog kapni?"))
print("Ennyivel fog növekedni a fizetése: ", (fizetés/100)*emelés,"Ft")

pénz= int (input("Mennyi pénzt tudsz félretenni egy hónapban?"))
laptop=int(input("Mennyibe kerül a laptop?"))
print(math.ceil(laptop/pénz),"Hónapig kell még rá gyüjtened")

kölcsön= int (input("Kérem a kölcsön összegét!"))
futam=int (input("Kérem a hátramaradó futamidőt!"))
print("A havi törlesztő:", (kölcsön/futam)/12, "ft")


szélesség=int (input("Adja meg a szoba szélességét!"))
magasság=int(input("Kérem a szoba magasságát!"))
csempe= ((szélesség*magasság)/(20*20)*1.1 )

print(math.ceil(csempe), " csempe szükséges ehez a szobához!")

óra=int (input("Kérem az órát!"))
perc= int (input("Kérem a percet"))
mp=int (input("Kérem a másodpercet"))
óra1=int (input("Kérem az órát!"))
perc1= int (input("Kérem a percet"))
mp1=int (input("Kérem a másodpercet"))
megoldás= ((óra*3600)+(perc*60)+mp)-((óra1*3600)+(perc1*60)+mp1)
print (megoldás,"a különbség")

átmérő=int (input("Kérem a dinnye átmérőjét"))
darab=int(input("Hány darab dinnye van?"))
csomagolás= (átmérő*2+60)*darab
print(csomagolás," cm csomagloás kell a dinnyékhez")

hossz=int(input("Kérem a kert hosszát!"))
szélesség=int(input("Kérem a kert szélességét!"))
négyzetméter=hossz*szélesség
print(math.ceil(négyzetméter/5))

gyök=int(input("Kérek egy számot"))
gyök2=int(input("Kérek ismét egy számot"))
print("A két szám négyzetgyöke:",sqrt(gyök+gyök2))

valós=float(input ("Valós számot kérek!"))
print(round(valós,2 ))

sík=float(input("Kordinátát kérek"))
sík2=float(input("Kordinátát kérek"))
print(sík-sík2, "a távolság")

név= input("Kérem a nevét!")
tömeg=int (input("Kérem a testtömeget!"))
magasság=float (input("Kérem a testmagasságot!"))
tti= tömeg/(magasság*magasság)
print(név,tti , "A testömeg indexed ")

havi=int(input("Havi villanyszámlát kérem"))
print("Az éves energiaköltség Kwh-ban:" ,havi*12)

ingatlanérték=int (input("Kérem adja meg a vásárolni kívánt ingatlan értékét!"))
ügynök= ingatlanérték*0.0275
ügyvéddíj=ingatlanérték*0.015
illeték=ingatlanérték*0.04
egyéb=46600
print("Az összköltség:" ,ingatlanérték+ ügyvéddíj+illeték+egyéb)









