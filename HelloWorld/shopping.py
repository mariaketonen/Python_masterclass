shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for loop to exclude spam from shopping list
for item in shopping_list:
    if item != "spam":
        print("Buy " + item)

# continue is not necessary, but will do the same as above
for item in shopping_list:
    if item == "spam":
        continue

    print("Buy " + item)

# break will stop the execution
for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)