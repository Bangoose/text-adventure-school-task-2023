import random

tilfeldig_tall=random.randint(1,1000000)

attempts = 0
attempts=int(attempts)
#print(tilfeldig_tall)

while True:
    attempts += 1
    Tall = input("gjett tall (1-1000000)")
    Tall = int(Tall)


    
    if Tall < tilfeldig_tall:
        print("too low")
       
    if Tall > tilfeldig_tall:
        print("too high")

    if Tall == tilfeldig_tall:
        print("ok")
        break