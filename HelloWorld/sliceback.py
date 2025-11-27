letters = "abcdefghijklmnopqrstuvwxyz"
        #  01234567890123456789012345
backwards = letters[25:0:-1]
print(backwards)
backwards = letters[25::-1]
print(backwards)
backwards = letters[::-1]
print(backwards)

backwards = letters[16:13:-1] # print qpo
print(backwards)
backwards = letters[4::-1] # print edcba
print(backwards)
backwards = letters[25:17:-1] # print the last 8 characters
print(backwards)
print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])

print(letters[-4:]) # last 4 characters
print(letters[-1:]) # last letter
print(letters[:1]) # first letter, not crashing if the string is empty
print(letters[0]) # first letter, crashes if empty

