'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1,1,0])
youstr = input("Enter Your choice: ")
youDict = {"s": 1, "w":-1, "g":0}
reverseDict = {1:"Snake", -1: "Water", 0 : "Gun" }

you = youDict[youstr]

print(f"you Chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")
#print("you Chose", dict, you\n, "Computer Chose", reverseDict, Computer")


if(computer == you):
    print("Its Draww")

else:
    if(computer == -1 and you == 1):
        print("You win.!!")

    elif(computer == -1 and you == 0):
        print("You Loose.!!")

    elif(computer == 1 and you == -1):
        print("You Loose.!!")

    elif(computer == 1 and you == 0):
        print("You Win.!!")

    elif(computer == 0 and you == -1):
        print("You win.!!")
        
    elif(computer == 0 and you == 1):
        print("You Loose.!!")

    else:
        print("sometings went Wrong")