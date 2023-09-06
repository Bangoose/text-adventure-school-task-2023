 
# lag et program som spør om navn og alder 
# og deretter skriver det ut i en setning med bare 1 print
navn = input("Hva heter du? -> ")
alder = input("Hvor gammel er du? -> ")
 
print("Hei " + navn + ", så hyggelig å snakke med deg. Du er", alder, "år")
 
# gjør om teksten alder til int
alder = int(alder)
 
# hvis vi er over 18 år skal vi få en beskjed om det
 
if alder >= 18:
    print("Du er over 18")
 
# om 100 år er jeg :
print("Om 100 år er du ", alder + 100, " år.")