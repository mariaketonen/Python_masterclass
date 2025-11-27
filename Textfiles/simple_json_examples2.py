import json
# list of tuples
languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]
# first creating the file, then reading the file and data in that
with open('test2.json', 'w', encoding='utf-8') as testfile:
    json.dump(languages, testfile)

with open('test2.json', 'r', encoding='utf-8') as testfile:
    data = json.load(testfile)
print(data)
print(data[2])
