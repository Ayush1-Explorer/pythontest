# st = ""
# f = open("hiscore.txt", "w")
# f.write(st)
# f.close()

# uncomment the abpve lines and run them first and then then run below code or else check out game1.py if u are too lazy to do it manually

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
            
            
