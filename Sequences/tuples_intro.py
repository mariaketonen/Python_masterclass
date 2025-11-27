#t = ("a", "b", "c") # parenthesis not required
#print(t) # tuple, not a list

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

#metallica[0] = "Master of Puppets" # cannot do this with tuples

metallica2 = list(metallica) # making a list instead
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2) # data is now incorrect, album was released in 1986

