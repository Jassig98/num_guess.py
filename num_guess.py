# Author: Jasmine Singh
# Github username: Jassig98
# Date: October 12, 2022
# Description: Project 3b

N=int(input("Enter the integer for the player to guess."))
count=0
guess=int(input("Enter your guess."))
while(True):
    count=count+1
    if(guess>N):
        guess=int(input("Too high-try again:"))
        continue
    elif(guess<N):
        guess=int(input("Too low-try again"))
        continue
    else:
        break
print("You guessed in in", count, "tries")
