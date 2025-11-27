menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(meals)
# conditional expression
# meals = [meal for meal in menu if "spam" not in meal]
meals = [meal if "spam" not in meal else "a meal skipped" for meal in menu]
print(meals)

x = 12
expression = "Twelve" if x == 12 else "unknown"
print(expression)

for meal in menu:
    print(meal, "contains chicken" if "chicken" in meal
    else "contains bacon" if "bacon" in meal else "contains eggs")

print()

items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)
print()
# a better way to do the listing on lines 29-31:
for meal in menu:
    for item in items:
        if item in meal:
            print("{} contains {}".format(meal, item))
            break
