
def show_menu(speisen):
    print("         Willkommen bei Acasa")
    stars()
    print("               Pizzen")
    for i in range(0, 3):
        print(speisen[i][0], " - ", speisen[i][1], ": ", speisen[i][2], "Euro")
    stars()
    print("              Aufläufe")
    for i in range(3, 5):
        print(speisen[i][0], " - ", speisen[i][1], ": ", speisen[i][2], "Euro")
    stars()
    order(speisen)


def order(speisen):
    bestellung = []
    while (True):
        wahl = int(input("Bitte fügen Sie die Nummer der Speise der Bestellung zu, mit 0 beenden Sie die Bestellung "))
        if wahl == 0:
            break
        bestellung.append(wahl)
    recipe(bestellung, speisen)


def recipe(bestellung, speisen):
    stars()
    print("Ihre Bestellung lautet:")
    summe = 0
    rechnung=[]

    for i in bestellung:
        for j in range(len(speisen)):
            if i == speisen[j][0]:
                print(speisen[j][0], speisen[j][1], speisen[j][2], "€")
                posten=(speisen[j][0], speisen[j][1], speisen[j][2])
                rechnung.append(posten)
                summe += speisen[j][2]
    stars()
    print_recipe(rechnung)
    print("Bitte bezahlen Sie", summe, "€ als Gesamtsumme")

def print_recipe(rechnung):
    import datetime

    timestamp = datetime.datetime.now()
    zeit = timestamp.strftime("%H:%M:%S %d.%m.%Y ")
    log = open("log.txt", mode="a")
    log.write(zeit)
    text = " " + str(rechnung) + "\n"
    log.write(text)
    log.close()


def stars():
    print("****************************************")


def main():
    speisen = [[100, "Pizza Margerita", 3], [101, "Pizza Thunfisch", 5], [102, "Pizza Funghi", 7],
               [200, "Auflauf mit Nudeln", 5], [201, "Auflauf mit Kartoffeln", 7]]

    show_menu(speisen)


if __name__ == '__main__':
    main()
