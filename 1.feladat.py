def beolvasas(file_neve):
    adatok = []
    with open(file_neve, "r", encoding='utf-8') as file:
        next(file) 
        for sor in file:
            parts = sor.strip().split(", ")
            if len(parts) == 4:
                talalmany, feltalalo, evszam, hely = parts
                try:
                    evszam = int(evszam)
                except ValueError:
                    continue 
                adatok.append((talalmany, feltalalo, evszam, hely))
    return adatok
def minden_adat_listazasa(adatok):
    for talalmany, feltalalo, evszam, hely in adatok:
        print(f"{talalmany} ({evszam}, {feltalalo}, {hely})")

def adatok_mentese(adatok):
    file_nev = input("Add meg a kimeneti fájl nevét: ")
    with open(file_nev, "w", encoding='utf-8') as file:
        for talalmany, feltalalo, evszam, hely in adatok:
            file.write(f"{talalmany} ({evszam}, {feltalalo}, {hely})\n")

def idotartomanyban_levo_vivmanyok(adatok):
    kezdo_ev = int(input("Add meg a kezdőévet: "))
    vegso_ev = int(input("Add meg a végsőévet: "))
    for talalmany, feltalalo, evszam, hely in adatok:
        if kezdo_ev <= evszam <= vegso_ev:
            print(f"{talalmany} ({evszam}, {feltalalo}, {hely})")

def menu():
    adatok = beolvasas("adatok.txt")
    while True:
        print("\n1. Minden adat listázása a képernyőre")
        print("2. Minden adat listázása egy fájlba")
        print("3. Adott időtartományban lévő vívmányok listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy opciót: ")

        if valasztas == '1':
            minden_adat_listazasa(adatok)
        elif valasztas == '2':
            adatok_mentese(adatok)
        elif valasztas == '3':
            idotartomanyban_levo_vivmanyok(adatok)
        elif valasztas == '4':
            break
        else:
            print("Érvénytelen választás.")
if __name__ == "__main__":
    menu()