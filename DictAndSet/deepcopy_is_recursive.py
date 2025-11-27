from simple_deepcopy import my_deepcopy
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original["Tim"].append("Australia")
original["J-P"].append("UK")
# two ways to add a value to the second index in the dict
original["Tim"][1].append("Cashier")
jp_list = original["J-P"]
jp_list[1].append("Courier")

print(original)
print(copy_1) # deepcopy does not change with the added values
print(copy_2) # shallow copy is referencing to the original values