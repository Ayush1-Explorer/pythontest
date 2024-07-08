import random
import os

# Ensure the hiscore.txt file exists
if not os.path.exists("hiscore1.txt"):
    with open("hiscore1.txt", "w") as f:
        f.write("")

def game():
    print("You are playing a game...")
    score = random.randint(0, 99)
    
    # Read the high score from the file
    with open("hiscore1.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0
    
    print(f"Your score: {score}")
    
    # Update the high score if the current score is greater
    if score > hiscore:
        with open("hiscore1.txt", "w") as f:
            f.write(str(score))
        print("New high score!")
    else:
        print("Try again to beat the high score!")
    
    return score

game()
