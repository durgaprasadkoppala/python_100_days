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

options = [rock, paper, scissors]
your_number = int(input(print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")))
if your_number > 0 and your_number<0:
    print("You typed an invalid number, you loose!")
else:
    you = options[your_number]
    print(you)
    computer = random.randint(0,2)
    print(f"Computer choose:{options[computer]}")
    
    if your_number == 0:
        if computer == 0:
            print("It's a draw")
        elif computer == 1:
            print("You loose")
        else:
            print("You Win")
    elif your_number == 1:
        if computer == 0:
            print("You Win")
        elif computer == 1:
            print("It's a draw")
        else:
            print("You Loose")
    elif your_number == 2:
        if computer == 0:
            print("You Loose")
        elif computer == 1:
            print("You Win")
        else:
            print("It's a draw")





        
    