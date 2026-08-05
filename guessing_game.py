guessing_game.

import random
number = random.randint(1, 10)
tries = int(input("How many attempts do you need to guess the number? "))
attempts = 0
while attempts < tries:
  print("====Guessing game====")
  guess = int(input("Enter a number betweeen 1, 10: "))
  attempts += 1
  if guess < number:
    print("Too Low.")
  elif guess > tries:
    print("Too high.")
  elif guess == number:
    print("Congratulations!")
    break
  else:
    continue
  print("attempts", attempts, "done.")
if guess != number:
    print("Game over! ")
    print("The correct number was: ", number)
    
