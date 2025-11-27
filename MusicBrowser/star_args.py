#print("Hello", "Planet", "Earth")

def average(*args):
    print(type(args))
    print("args is: {} ".format(args)) # tuple given
    print("*args is:", *args) # unpacking the tuple of numbers
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)

print(average(1, 2, 3, 4))

def build_tuple(*args):
    return args

message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message_tuple))
print(message_tuple)
print(message_tuple[::-1])

number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)
# *args unpacks tuple, **kwargs unpacks dictionary
#def print_backwards(*args, **kwargs):
#    print(kwargs)
#    kwargs.pop('end', None)
#    for word in args[::-1]:
#        print(word[::-1], end=' ', **kwargs)


def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for world in args[:0:-1]:
        print(world[::-1], end=sep_character, **kwargs)
    # print(end=end_character)
    print(args[0][::-1], end=end_character, **kwargs)


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another String")

print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n', sep='|')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n', sep='|')

print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 10)
