print("du drikker ett glass med melk og går derreter til en skog hvor du går deg vill. Du er nå sulten, og må få i deg litt mat")
print("Etter hvert finner du en bær busk.")

valg = input("Hva gjør du?  A: Spis det  B: Ignorer det --> ")

if valg == "A":
    print("Etter å ha spist litt ble du veldig uggen i magen.")

    valg = input ("hva gjør du nå? A: Spis mere  B: dra videre")

    if valg == "A":
        print("Du var bare dårlig i magen siden du var laktose intollerant,")


if valg == "B":
    print("Du spiste ikke og derfor sultet hjel... du døde, prøv igjen.")

if valg == "C":
    print("ka du driv på med? dette var ikke ett gyldig valg, en bjørn kommer og spiser deg.")
    valg = input ("A: Dø  B: Dø --> ")

    if valg == "A":
        print("Du døde")
    
    if valg == "B":
        print("Du døde")

    if valg == "C":
        print("bjørnen så deg og mistet matlysten... den stakk (dette ekke greit, slutt å velge noe som ikke er ett valg)")
        