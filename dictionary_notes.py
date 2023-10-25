# capital_cities = {
#     "England" : "London",
#     "Scotland" : "Edinburgh",
#     "Wales" : "Cardiff",
#     "Northern Ireland" : "Belfast",
#     "Ireland" : "Dublin"
#     }

# KEY must be immutable data type- can't be changed
# can only add and remove keys

# VALUE can be any data type

# capital_cities = {
#     "England" : "London",
#     "Scotland" : "Edinburgh",
#     "Wales" : "Cardiff",
#     "Northern Ireland" : "Belfast",
#     "Ireland" : "Dublin"
#     }

# print(capital_cities["England"])

animal_offspring = {
    "Dog" : "Puppy",
    "Lion" : "Cub",
    "Sheep" : "Lamb",
    "Pig" : "Piglet"
}

# print(animal_offspring["Pig"])

# animal_offspring["Dog"] = "baby dog"

# print(animal_offspring)

# . keys() method- will give a list of all the keys in the dictionary 
# print(animal_offspring.keys())
# print(animal_offspring.values())
# key:value = called Item
# print(animal_offspring.items())

# print(animal_offspring.get("Dog"))
# print(animal_offspring["Dog"])

# print(animal_offspring.get("Dragon"))- None. No data to give back. safer to keep code in, return none instead of crashing
# print(animal_offspring["Dragon"])- gives error- crashes so doesn't cause more damage 

# print(animal_offspring.get("Dragon", "We couldn't find a baby animal for that parent"))
# give .get 2 aruguments - get a response if value not there

# print(animal_offspring.setdefault("Pigeon", "Squab"))
# print(animal_offspring)

animal_offspring.setdefault("Pigeon", "Squab")

print(animal_offspring)
# adds to the dictionary and also keeps safe from unwanted changes. Will add key and value if not already there
# won't let you chnage value if key already exists

# can change value using .update() method
# animal.update({"Fish : Fry}, "Crab : "Zoea"})- will add to the animal dictionary, with a new one

animal_offspring.update({"Lion" : "Baby Lion"})
# added to the end of the dictionary, and in python will use the last(most recent)update- therefore Baby Lion will show
print(animal_offspring)

# animal_offspring.pop()
# In list will get rid of last item or can use index position number to find item. However don't have index number in dictionary, we have a KEY.
# animal_offspring.pop("Dog")

# print(animal_offspring)

# animal_offspring.popitem()- last one of the dictionary is removed 