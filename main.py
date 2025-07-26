import random
Rock="""
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
Scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_print = [Rock, Paper, Scissors]
total = 0
user_total = 0

while (total < 5) :
    total += 1
    print(total)
    computor_choice = random.randint(0, 2)
    print("welcome to the Rock Paper Scissors Game!")
    user_choice = input("Which one you choose? \nRock for 0, \nPaper for 1, \nScissors for 2: \n")
    if 0 <= int(user_choice) < 3  :
        user_choice = int(user_choice)
        print(game_print[user_choice])
        print("Vs")
        print(game_print[computor_choice])
        if user_choice == 0 and computor_choice == 2:
            user_total += 1
            print("You win.")
        elif user_choice == 2 and computor_choice == 0:
            print("You loss.")
        elif user_choice == computor_choice:
            print("Draw")
        elif user_choice > computor_choice:
            user_total += 1
            print("You win.")
        else:
            print("you loss.")
        print(f"your total score is  {user_total}.")
    else :
        print("Please choose right one.")




