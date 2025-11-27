from contents import pantry
# printing out the quantity of existing key in dict:
chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")
# setdefault adds the key to the dict:
beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")
# get does not add the key to the dict:
ketchup_quantity = pantry.get("ketchup", 0)
print(f"Ketchup: {ketchup_quantity}")
# adding a value to the key zucchini:
z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")

print()
print("`pantry`now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)