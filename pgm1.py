import random

random = random.randint(1, 10)

while True:
    guess = int(input("enter your guess number "))

    if guess == random:
        print("you won bravo")
        break
    if guess < random:
        print("your guess is less")
    if guess > random:
        print("your guess is large")

print("gameover")
