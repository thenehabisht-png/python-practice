'''
1 for snake
-1 for water
0 for gun
'''
import random

while True:
    computer = random.choice([-1, 0, 1])

    youstr = input("Enter your choice (snake/water/gun): ").lower()

    if youstr not in ["snake", "water", "gun"]:
        print("Invalid choice!")
        continue

    youDict = {"snake": 1, "water": -1, "gun": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    you = youDict[youstr]

    print(f"You chose: {reverseDict[you]}")
    print(f"Computer chose: {reverseDict[computer]}")

    
    if(computer == you):
        print("Its a draw")

    elif(computer  == -1 and you == 1):
        print("You Win!")
    elif(computer  == -1 and you == 0):
        print("You Lose!")
    elif(computer  == 1 and you == -1):
        print("You Lose!")
    elif(computer  == 1 and you == 0):
        print("You Win!")
    elif(computer  == 0 and you == -1):
        print("You Win!")
    elif(computer  == 0 and you == 1):
        print("You Lose!")
    else:
        print("Something went Wrong!")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break