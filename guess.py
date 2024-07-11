import random
n = random.randint(1, 100)


a = -1
guesses = 0
while(a != n):
    a = int(input("Guess The Number: "))
    guesses += 1
    if(a < n):
        print("Higher Number Please.")
    else:
        print("Lower Number Please.")
        
if(a == n):
    print(f"You have guessed it right {n} in {guesses} attempts.")
