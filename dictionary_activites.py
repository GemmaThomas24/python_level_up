# Challenge 1
# fav_song = {
#     "Britney Spears" : "I'm not a Girl",
#     "BTS" : "Euphoria",
#     "Jung Kook" : "3D",
#     "V" : "Slow Dancing"
# }

# fav_song.update({"Beyonce" : "Ava Maria", "Maxwell" : "This Womens Work"})
# print(fav_song)
# {} after.update as adding a new dictionary

# Challange 1 stretch
# fav_song = {
#     "Britney Spears" : "I'm not a Girl",
#     "BTS" : "Euphoria",
#     "Jung Kook" : "3D",
#     "V" : "Slow Dancing"
# }

# for x, y in fav_song.items():
#     print(x, y)

# for i in fav_song
# print(fav_song.keys())
# print(fav_song.values())
# print(fav_song.items())- this combines the keys/values

# for k,v in fav_song.items():
#     print(f"Artist: {k}  - Song: {v}")

# Challenge 2

# countries = ["England", "Spain", "Ethiopia", "Iran"]
# languages = ["English", "Spanish", "Amharic", "Farsi"]

# dictionary = dict(zip(countries,languages))
# print(dictionary)

# found this example but not as strightforward as the one above.
# d = {}
# # # d{} initalizes an empty dictionary named 'd'

# for k,v in zip(countries,languages):
#     d[k] = v
# print(d)    

# Challenge 3

# animal_offspring = {
#     "Dog" : "Puppy",
#     "Lion" : "Cub",
#     "Sheep" : "Lamb",
#     "Pig" : "Piglet"
# }

# print(animal_offspring.get())- returns the value of the Key. If Key not there, returns None.
# animal = input("Enter the name of an animal  >  ").capitalize()
# print(animal.get(animal_offspring, "We couldn't find a baby animal for that parent"))


# seperate
# animal = input("Enter the name of an animal  >  ")
# if animal in animal_offspring:
#     print(animal_offspring[animal])
# else:
#     print("Sorry we do not have infomation on this animal")  


# Challenge 4
animal_offspring = {
    "Dog" : "Puppy",
    "Lion" : "Cub",
    "Sheep" : "Lamb",
    "Pig" : "Piglet"
}

animal = input("Enter the name of an animal  >  ").capitalize()
offspring = input("Enter term for animal offsrping  >  ").capitalize()

if animal in animal_offspring:
    print(animal_offspring[animal])
else:
    animal_offspring.setdefault(animal, offspring)

print(animal_offspring)
# need to look at this, something not quite right