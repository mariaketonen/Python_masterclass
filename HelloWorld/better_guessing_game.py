import random

highest = 10
answer = random.randint(1, highest)
#print(answer)

#print("Please guess number between 1 and {}: ".format(highest))
#guess = int(input()) # TODO: remove after testing

#if guess == answer:
#    print("You got it the first time!")
#else:
#    if guess < answer:
#        print("Please guess higher")
#    else:   # guess must be greater than answer
#        print("Please guess lower")
#    guess = int(input())
#    if guess == answer:
#        print("Well done, you guessed it")
#    else:
#        print("Sorry, you have not guessed correctly")

# challenge for guessing game to continue until guessed right

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

while guess != answer:
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you have not guessed correctly")

# or you can do it this way

guess = 0
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess =int(input())

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
