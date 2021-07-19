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
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
comp = random.randint(0, 2)
if your_choice == 0 and comp == 1:
  print(f"You choose rock{rock}\nYour computer chosen paper {paper}.\nYou lose.")
elif your_choice == 1 and comp == 2:
  print(f"You choose paper{paper}\nYour computer chosen scissors {scissors}.\nYou lose.")
elif your_choice == 2 and comp == 0:
  print(f"You choose scissors{scissors}\nYour computer chosen rock {rock}.\nYou lose.")
elif your_choice == 1 and comp == 0:
  print(f"You choose paper{paper}\nYour computer chosen rock {rock}.\nYou win.")
elif your_choice == 2 and comp == 1:
  print(f"You choose scissors{scissors}\nYour computer chosen paper  paper{paper}.\nYou win.")
elif your_choice == 0 and comp == 2:
  print(f"You choose rock{rock}\nYour computer chosen scissors {scissors}.\nYou win.")  
else:
 print("Both you have chosen the same. No one win!")






