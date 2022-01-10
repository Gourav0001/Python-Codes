# Snake Water Gun Game with 10 rounds

import random

print ("This game will have 10 rounds.")
win = 0
lost = 0
Draw = 0

for t in range (10):
    List = ["Snake", "Water", "Gun"]
    AI = random.choice(List)
    print("Please Write Your Choice ")
    You = input()
    while AI == "Snake":
        if You == "Gun":
            print ("You win.")
            win += 1
            break
        elif You == "Water":
            print ("You lost.")
            lost += 1
            break
        else:
            print ("Tie")
            Draw += 1
            break

    while AI == "Gun":
        if You == "Water":
            print("You win.")
            win += 1
            break
        elif You == "Snake":
            print("You lost.")
            lost += 1
            break
        else:
            print("Tie.")
            Draw += 1
            break
    while AI == "Water":
        if You == "Snake":
            print("You win.")
            win += 1
            break
        elif You == "Gun":
            print("You lost.")
            lost += 1
            break
        else:
            print("Tie")
            Draw += 1
            break
print (" ")
if win > lost:
    print ("You Won! Congrats!")
elif lost > win:
    print ("You loose! Better Luck Next Time!")
else:
    print ("Match Draw")

print ("Scores")
print (win)
print (lost)
print (Draw)
