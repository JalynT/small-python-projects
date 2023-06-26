#User has 3 guesses
#if guess is wrong, loop keeps running
#if guess is right, loop ends
import random

secretNum = random.randint(0, 9)
i = 0

print("WELCOME TO GUESS!!! GUESS ANY NUMBER FROM 0-9!")

while i < 3:
  guess = int(input("Guess: "))
  if guess == secretNum:
    i = 3
    print("You Win!")
  i+= 1
  
if guess!= secretNum:
  print("Sorry you failed!")
