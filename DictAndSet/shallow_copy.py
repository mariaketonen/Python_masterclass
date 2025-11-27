import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}
# shallow copy of the dict
# things = animals.copy()
# animals["teddy"] = "toy"

# Perform a deep copy
things = copy.deepcopy(animals)

print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print()

things["teddy"].append("toy") # adding a value to the key
print(things["teddy"])
print(animals["teddy"])