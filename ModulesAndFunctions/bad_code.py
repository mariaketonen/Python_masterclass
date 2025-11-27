area = 0 # area is bound globally to 0


def area_of_square(length: float):
    #area = length * length
    global area # changed scope DO NOT DO IT LIKE THIS
    area = length * length


area_of_square(30)
print(f'The area is {area}')