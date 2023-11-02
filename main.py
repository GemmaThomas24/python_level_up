from person import Person
# from file person import person class
# person.py has the blueprint. main.py does the building
# if something wrong with blueprint, know where to go- that's why keep seperate

# liam = Person("Liam", 30, "Tall")

# print(liam.height)
# print(liam.name)
# print(liam.age)


gemma = Person("Gemma",26, "5ft 7")

# print((f"My name is {gemma.name}, I am {gemma.age} years old and I am {gemma.height} tall"))

# gemma.introduce()

# gemma.name = "Wendy"

# print(gemma.name)

gemma.set_new_name("Wendy")

print(gemma.name)



