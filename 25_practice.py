#Write a program to print the game()function lets a user play a game and return the score as integer .
# You need to read a file 'Hi-score.txt'which is either blank or contain to update Hi-score when game()function breaks Hi score
import random
def game():
    print("You are playing the game")
    Score=random.randint(1,62)
with open("hiscore.txt")as f:
    hiscore=f.read()
if (hiscore!=""):
    hiscore=int(hiscore)
else:
    hiscore=0
print(f"Your score:{Score}")  
with open("hiscore.txt","w")as f:
    f.write(str(score))
return Score
Game()



