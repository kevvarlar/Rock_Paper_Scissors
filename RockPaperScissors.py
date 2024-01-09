import random
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
RPS = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
user = int(input())
comp = random.randint(0, 2)
print(RPS[user])
print("Computer chose:")
print(RPS[comp])
if user == 0:
    if comp == 0:
        print("It's a draw!")
    elif comp == 1:
        print("You lose!")
    else:
        print("You win!")
if user == 1:
    if comp == 1:
        print("It's a draw!")
    elif comp == 2:
        print("You lose!")
    else:
        print("You win!")
if user == 2:
    if comp == 2:
        print("It's a draw!")
    elif comp == 0:
        print("You lose!")
    else:
        print("You win!")
