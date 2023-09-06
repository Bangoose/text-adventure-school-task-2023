print("Du går en tur i en skog, du har gått deg vill og må nå prøve å komme deg tilbake")

mat = 50
hp = 100
def maxhp():
    global hp
    if hp > 100:
        hp = 100
def maxmat():
    global mat
    if mat > 100:
        mat = 100

import random
def rom_1():
    print("Du finner en hytte")
    valg = input("Velg A for å prøve å gå inn i hytta eller B for å gå videre og leite etter ett bedre utkjiks punkt --> ").upper()
    if valg == "A":
        rom_2()
    if valg == "B":
        rom_3()

def rom_2():
    print("Døra er kilt fast, du feiler på å åpne den, vill du prøve igjen?")
    valg = input("A for å prøve igjen, B for å gå videre--> ").upper()
    if valg == "A":
        rom_2()
    if valg == "B":
        rom_3()
    if valg == "C":
        print("dette er ikke ett valg, prøv igjen")

def rom_3():
    global hp
    print("du gikk videre, etter en tid med gåing er du sulten.")
    valg = input("du finner mat på bakken, det er litt frukt og en mugglete brødskive, hva vill du gjøre? A. Spis begge. B. Spis fruken. C. Spis brødskiva.").upper()
    if valg == "A":
        dmg = random.randint(1, 50)
        hp -= dmg
        print(f"Du fikk matforgiftning og mister derfor {dmg} helse du har nå {hp} liv igjen")
    if valg == "B":
        print ("Du spiser frukten og blir mett")

    if hp <=0:
        game_over()

    def game_over():
        print("du sug")
        exit()

rom_1()