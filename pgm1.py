import random

random = random.randint(1, 10)

while True:
    guess = int(input("enter your guess"))

    if guess == random:
        print("your guess is correct")
        break
    elif guess < random:
        print("guess is less")
    elif guess > random:
        print("guess is greater")

print("gameover")
