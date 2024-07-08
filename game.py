import random

def game():
    print("you are playing a game...")
    score = random.randint(0, 99)
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
            
    print(f"your score: {score}")
    if(score > hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
            
    return score

game()
            
            
