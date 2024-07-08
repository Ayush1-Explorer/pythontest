import random

'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
yourDict = {"s": 1, "w": -1, "g": 0}
reversedict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = yourDict[youstr]

print(f"You Chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if(computer == you):
    print("Its An Draw")
else:
    if(computer - you == -1 or computer - you == 2):
        print("You Lose!")
    elif(computer - you == 1 or computer - you == -2):
        print("You Won")
    # for the above logic that you will lose if you got -1 and 2 by calculating the numbers in write fights 
    # and you win when u get 1 and -2 when the calculations are right and this is the short way than using if else ladder.
    
    # if(computer == -1 and  you == 1):
    #     print("You Win")
    # elif(computer == 1 and you == -1):
    #     print("You Lose!")
    # elif(computer == 1 and you == 0):
    #     print("You Win")
    # elif(computer == 0 and you == 1):
    #     print("You Lose!")
    # elif(computer == -1 and you == 0):
    #     print("You Lose!")
    # elif(computer == 0 and you == -1):
    #     print("You Win")
    else:
        print("Something Went Wrong.")
        
