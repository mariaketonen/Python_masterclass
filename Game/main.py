from enemy import Enemy, Troll, Vampyre, VampyreKing

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))
another_troll.take_damage(18)

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

vampyre = Vampyre("Jonathan")
print(vampyre)

vampyre.take_damage(5)
print(vampyre)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)

while vampyre.alive:
    vampyre.take_damage(1)
    print(vampyre)

dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)

# you should refactor the attributes starting with _
# so they cannot be changed
# but this may need some extra work afterward
#vampyre.lives = 0
#vampyre.hit_points = 1
#print(vampyre)