numbers = {} # is NOT an empty set
print(numbers, type(numbers))

numbers = {*""} # Do NOT use this to create an empty set
print(numbers, type(numbers))

numbers = {*{}} # Still NOT a good way to do it
print(numbers, type(numbers))

numbers = set() # empty set
print(numbers, type(numbers))

numbers.add(1) # adding a number to the set
print(numbers)
# add numbers to the set until there are four unique values
while len(numbers) < 4:
    next_value = int(input("Please enter your next value: "))
    numbers.add(next_value)
print(numbers)