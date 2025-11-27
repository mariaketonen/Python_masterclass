import random


def get_integer(promt):
    while True:
        temp = input(promt)
        if temp.isnumeric():
            return int(temp)
        else:
            #print("Please enter a valid number.")
            print("{0} is not a valid number".format(temp))


highest = 1000
answer = random.randint(1, highest)

guess = 0
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0: # if they cannot guess, they can get out by typing 0
        break
    if guess == answer:
        print("Well done, you guessed it!")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        elif guess > answer:
            print("Please guess lower")
