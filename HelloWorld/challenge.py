list_of_items = ["Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed"]

chosen_item = ""
while chosen_item not in list_of_items:
    chosen_item = input("Please choose an item from the list {}: ".format(list_of_items))
    if chosen_item.casefold() == "0":
        print("Game Over")
        break
else:
    print("Well chosen, {} is a valid option!".format(chosen_item))

# Solution
# You can also use while True with conditions

choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("6:\tExit")
    choice = input()
