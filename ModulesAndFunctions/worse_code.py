area = 0 # area is bound globally to 0
length = 30 # length is now globally bound to 30


def area_of_square():
    #area = length * length
    global area # changed scope DO NOT DO IT LIKE THIS
    area = length * length


area_of_square()
print(f'The area is {area}')