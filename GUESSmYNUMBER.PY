import random

compno = random.randint(1,10)
while True :
  guessno = int(input('enter your guess number'))
  if guessno == compno:
    print('your guess number is right congrats you won')
    break
  elif guessno > compno:
    print('your guess number is greater than computer generated number choose a lower guess')
  else:
    print('your guess number is lower than computer generated number guess a higher number')  