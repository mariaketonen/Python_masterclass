#jabber = open('Jabberwocky.txt', 'r') # r means read (=default)

#for line in jabber:
    #print(line.strip())
    #print(line, end='')
    #print(len(line))
# if you open a file, you need to close it as well
#jabber.close()
# automatically close the file when it has been read
#with open('Jabberwocky.txt', 'r') as jabber:
    #for line in jabber:
    #    print(line.rstrip())
#    lines = jabber.readlines()

#print(lines) # prints a list of strings
#print(lines[-1:]) # last line, string
#for line in reversed(lines):
#    print(line, end='') # reversed order

#with open('Jabberwocky.txt', 'r') as jabber:
#    text = jabber.read()

#print(text)

#for character in reversed(text):
#    print(character, end='')
# readline reads the file line by line
with open('Jabberwocky.txt') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)

with open('Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break