small_ints = set(range(21))
print(small_ints)
# Removing all items from the set
#small_ints.clear()
#print(small_ints)
# Removing individual items from the set
small_ints.discard(10)
small_ints.remove(11)
print(small_ints)
# If item not in the set, nothing is done
small_ints.discard(99)
print(small_ints)
# Remove will crash the program if item is not in the set
small_ints.remove(99)
print(small_ints)