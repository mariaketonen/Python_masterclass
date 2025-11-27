#           1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print()
print()
print()

print(parrot[0:6]) # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])

print(parrot[:6]) # from the start
print(parrot[6:]) # until the last

print(parrot[:6] + parrot[6:])
print(parrot[:])
      #    012345678901234567890123456
letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[5:26])
print(letters[-21:])
print(letters[7:10])
print(letters[-19:-16])

print(parrot[-4:-2]) # Bl
print(parrot[-4:12])
print(parrot[-14:-8])

# Steps

print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw

number = "9,223;372:036 854,775;807"
print(number[1::4])

separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
