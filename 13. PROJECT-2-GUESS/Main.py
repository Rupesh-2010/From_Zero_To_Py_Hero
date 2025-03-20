import random
N = random.randint(1,100)

A = -1
Guesses = 1
while(A != N):
    A = int(input("Guess The Number: "))
    if(A>N):
        print("LOWER NUMBER PLEASE.")
        Guesses +=1
    elif(A<N):
        print("HIGHER NUMBER PLEASE.")
        Guesses +=1

print("YOU GUESSED THE NUMBER" ,N, "CORRECTLY IN",Guesses, "ATTEMPTS")