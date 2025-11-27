name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("Congratulations {}, age {}, you are welcome!".format(name, age))
else:
    print("Sorry {}, you are not the right age at {}".format(name, age))
