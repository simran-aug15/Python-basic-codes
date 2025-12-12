#Write a program to print the game()function lets a user play a game and return the score as integer .
# You need to read a file 'Hi-score.txt'which is either blank or contain to update Hi-score when game()function breaks Hi score
import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 62)
    return score


# Read previous hi-score
try:
    with open("hiscore.txt", "r") as f:
        hiscore = f.read().strip()
        hiscore = int(hiscore) if hiscore else 0
except:
    hiscore = 0

# Play game
score = game()
print(f"Your Score: {score}")

# Update if new score is better
if score > hiscore:
    print("Congratulations! New High Score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
else:
    print("High Score remains:", hiscore)

