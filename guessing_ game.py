import random
a = random.randint(1, 10)
guess = 0
print("*This is a guessing game* You get 3 tries")

while guess < 3:
    usr = int(input("Try to guess a number between 1 and 10"))
    guess += 1
    if a == usr:
        print("You Won!")
        break
    elif guess >= 3:
        print("No Win this time")

    elif usr - a == 1 or usr - a == -1:
        print("You're heating up!")

    elif usr - a == 2 or usr - a == -2:
        print("You're getting warmer")

    elif usr - a > 2 or usr - a < -2:
        print("You're getting colder")
