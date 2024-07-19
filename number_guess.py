#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
print("Choose a difficulty. Type 'Easy' or 'Hard': ")
difficulty = input().lower()
print(number)
def easy():
  for a in range(10,0,-1):
    global number
    print(f"You have {a} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess<number:
      print("Too Low\nGuess again.")
    elif guess>number:
      print("Too High\nGuess again.")
    elif guess==number:
      print(f"You guessed right {guess} and you won!")
      break

def hard():
  for a in range(5,0,-1):
    global number
    print(f"You have {a} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess<number:
      print("Too Low\nGuess again.")
    elif guess>number:
      print("Too High\nGuess again.")
    elif guess==number:
      print(f"You guessed right, the answer was {guess}")
      break
if difficulty == "easy":
  easy()
else:
  hard()
