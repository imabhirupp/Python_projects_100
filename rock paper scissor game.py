rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("Enter your choice - rock or paper or scissors")
a = input()
if a == "rock":
    print(rock)
elif a =="paper":
    print(paper)
else:
    print(scissors)
b = random.randint(0,2)
c = [rock, paper, scissors]
d = c[b]
print(d)
if a=="rock" and d==rock:
    print("Draw")
elif a=="rock" and d==scissors:
    print("You win")
elif a=="rock" and d==paper:
    print("You lose")
elif a=="paper" and d==paper:
    print("Draw")
elif a=="paper" and d==rock:
    print("You Win")
elif a=="paper" and d==scissors:
    print("You loose")
elif a=="scissors" and d==scissors:
    print("Draw")
elif a=="scissors" and d==rock:
    print("You loose")
elif a=="scissors" and d==paper:
    print("You win")
