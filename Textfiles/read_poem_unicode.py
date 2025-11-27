with open('Jabberwocky.txt', encoding='utf-8') as jabber:
    for line in jabber:
        print(line.rstrip())
# this works on my Linux without the encoding specified
# test with encoding='utf-8' deleted