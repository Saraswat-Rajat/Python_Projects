# rock paper scissors


import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rps = [Rock, Paper, Scissors]


print("your choice")

choice = int(input("1 for rock, 2 for paper, 3 for scissors : "))

if (choice == 1):
    print("your choice : ")
    print(rps[0])
if (choice == 2):
    print("your choice : ")
    print(rps[1])
if (choice == 3):
    print("your choice : ")
    print(rps[2])

print("------------------------------")

num = random.randint(1, 3)
print("computer's choice")
print(rps[num-1])
print("------------------------------")

if (choice == 1 and num == 1):
    print("Draw")
if (choice == 1 and num == 2):
    print("Computer Won!")
if (choice == 1 and num == 3):
    print("You Won")
if (choice == 2 and num == 1):
    print("You Won")
if (choice == 2 and num == 2):
    print("Draw")
if (choice == 2 and num == 3):
    print("Computer Won")
if (choice == 3 and num == 1):
    print("Computer Won")
if (choice == 3 and num == 2):
    print("You Won")
if (choice == 3 and num == 3):
    print("Draw")
