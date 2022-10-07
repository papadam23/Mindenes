def fizetes():
    fizetes=int(input("Kérem a fizetését foritnban megadva"))
    if fizetes>500000:
        print("Az új fizetése:",+(fizetes+(fizetes*0.2)),"Ft")
    elif fizetes<500000:
        print("Az új fizetése:",+(fizetes+(fizetes*0.3)),"Ft")

def teglalap(aoldal,boldal):
    terulet=aoldal*boldal
    print(f"{aoldal}és {boldal}oldalú téglalap területe: {terulet}")




def main():
     
     teglalap(5,6)
     teglalap(8,10)


main()
