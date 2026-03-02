import random

print(" hi welcome to number guessing game")
guess = int(input("please guess the number"))
real = random.randint(1,100)
count = 1

while guess != real:
    if guess > real:
        print("please enter smaller value")
        guess = int(input("please guess the number"))
        count += 1
    else :
        print(" please enter bigger value")
        guess = int(input("please guess the number"))
        count +=1
else:
    print("you guessed it right . you guessed at", count , "th attempt")

    


