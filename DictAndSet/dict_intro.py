vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple',
}
# adding key+item to the dictionary
vehicles["toy"] = "Glider"
vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier LearJet 75"

# upgrade the value in dictionary
vehicles["virago"] = "Yamaha XV535"

# deleting an item in a dictionary
del vehicles["starfighter"]
# if the key does not exist, we want an output not crashing the program
#del vehicles["f1"]
result = vehicles.pop("f1", None)
print(result)
plane = vehicles.pop("learjet")
print(plane)
bike = vehicles.pop("tenere", "not present")
print(bike)
print()
# key and value are case sensitive
my_car = vehicles['fiesta'] # key to get the value
print(my_car)

commuter = vehicles['virago']
print(commuter)

learner = vehicles.get("er5") # dictionary get method
print(learner)
# print out the keys of the dictionary items
for key in vehicles:
    print(key)
    # print both key and value of the items with separator ", "
    print(key, vehicles[key], sep=", ")
# better way to print both key and value with separator ", "
for key, value in vehicles.items():
    print(key, value, sep=", ")