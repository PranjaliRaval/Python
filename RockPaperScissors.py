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
import random
game_images =[rock,paper,scissors]

user_choose = int(input("what do you choose? \n0.Rock \n1.Paper \n2.Scissors "))
if user_choose >=3 or user_choose < 0:
    print("You typed invalid number.You Loose!!!")
else:
    print(game_images[user_choose])


computer_choose = random.randint(0,1)
print("Computer Chose: ")
print(game_images[computer_choose])

if user_choose == 0 and computer_choose == 2:
    print("You won")

elif computer_choose == 0 and user_choose == 2:
    print("You won")
elif computer_choose > user_choose:
    print("You loose")
elif user_choose > computer_choose:
    print("You Won")
elif computer_choose == user_choose:
    print("Its a draw")
