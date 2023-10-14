import random
wlc = "Welcome To Guess The Number"
print(wlc.center(50))

gs = "Guess The Number From 1-20"
print(gs.center(50))

random = random.randint(1,20)

def game():
    for i in range(4):
        t1 = int(input("Guess The Number- "))
        if t1 == random:
            print("Yay you Guessed The Number It Was-",random)
            return
        elif t1 > random:
            print("Lower")
        else:
            print("Higher")
    print("You lose,The Number Was-",random)
    

game()