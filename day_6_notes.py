# Level up notes- Day 6
# TRUTHY/FALSEY

# music = "classical"
# shopping_list = []
# num = 0
# name = ""
# my_name ="Dave"

# print(bool("classical"))
# # cast to be a boolean
# print(bool(shopping_list))
# print(bool(num))
# print(bool(name))
# print(bool(my_name))

# empty sting/Intergers= Falsey/None

# name = input("please enter your name")

# if name:
#     print("Welcome to your account", name)
# else:
#     print("You did not give me a name")

# IN OPERATOR

# answer = input("what coat is always wet when you put it on?")

# if "paint" in answer:
#     print("Correct!")
# else:
#     print("Incorrect!")

# list of shopping items
# programme to allow user to add new items to list
# if item already in list, don't add

# shopping_list = [
#      "apples",
#      "pears",
#      "chocoate",
#      "bread"
#  ]

# addionional_items = input("Is there anything else you would like to purchase  >  ")

# shopping_list.append("Coke")
# print(shopping_list)

# if addionional_items in shopping_list:
#     print("You already have this item in the basket")
# else:
#     (addionional_items.append(""))


# Correct One
# shopping_list = [
#      "apples",
#      "pears",
#      "chocoate",
#      "bread"
#  ]

# addionional_items = input("Is there anything else you would like to purchase  >  ")

# # shopping_list.append(addionional_items)
# # print(shopping_list)

# if addionional_items in shopping_list:
#     print("You already have this item in your shopping list")
# else:
#     shopping_list.append(addionional_items)

# print(shopping_list)


# NOT OPERATOR
# allowed_answers =["Yes", "no", "Yeah", "Nope", "Okay"]

# answer = input(" What is your answer?")

# while answer not in allowed_answers:
#     print("that is not an acceptable anser!")
#     answer = input(" What is your answer?")
# else:
#     print("thank you for your response")

# FUNCTIONS-RETURN

# def add_up(num1,num2):
#     global answer
#     answer = num1+num2
#     print(answer)

# add_up(4,7)

# print(add_up(4,7))
# this example works but not effiencent- functions should be small and reusable and non-specific 

# def add_up(num1,num2):
#     return num1+num2

# add_up(4,7)
# print(add_up(4,7))

# user ro be able to withdrawn cash if pin is right

# def cash_machine:

# take user pin
# see if pin correct
# if pin correct let withdraw cash

# pin check function:
# see if pin is  correct

# cash function:
# once pin is correct let user withdraw

# def pin_checker(user_pin):
#     if user_pin == "1234":
#         return True
#     else:
#         return False
    
# def cash_withdraw(amount,user_pin):
#     if pin_checker(user_pin):
#         print(f"you can withdraw {amount}")
#     else:
#         print("Your pin is not correct")

# cash_withdraw(100, "1234")

# def chnage_pin(newpin, user_pin):
#     if pin_checker(user_pin):
# (let them change to new pin)


# list comprehension

# dinosaurs = [
#     "Triceratops",
#     "Velociraptor",
#     "Anklyosaurus",
#     "Archaeopteryx",
#     "Tyrannosaurus Rex",
#     "Stegosaurus",
#     "Iguanodon"
# ]
# for i in dinosaurs:
#     print(i)

# saurus_dinos =[]

# for dino in dinosaurs:
#     if "saurus" in dino:
#         saurus_dinos.append(dino)

# print(saurus_dinos)

# saurus_dinosaurs =[dino for dino in dinosaurs if "saurus" in dino]
# # same as for loop but in list format(list comprenshion)

# print(saurus_dinos)
# print(saurus_dinosaurs)

# LIST TUPLES

# coffee_order= (
#     "Alex - Cortado",
#     "Ben - Latte",
#     "Charlie - Mocha"
# )
# # () means it's a Tuples

# coffee_order.append("Diane - Hot Chocolate")

# print(coffee_order)
# Tuples are immutable data type, can't make changes, so .append won't work- can't use any methods to alter
# count and index, that give back properties of the collecion
# Tuples- keep data safe and you don't want to remove from/overwrite- data at risk. so unchangeable data type, locked in safely.



# WHILE LOOPS- TRUE AND BREAK

# print("type in two numbers to multipy them")

# while True:
#     try:
#         num1 = int(input("   >   "))
#         num2 = int(input("   >   "))
#         break
#     except ValueError:
#         print("Please use intergers only")

# print(num1*num2)

# Challange 1

# truthy_or_falsey = [0, "Hello!", " ", "!!", 12, True, None, "", "0", False, "False"]

# for i in truthy_or_falsey:
#     if i:
#         print(True)
#     else:
#         print(False)


# Challange 2

guest_name = input("What is your name?")

guest_list = [
    "Katy",
    "Geogia",
    "Louisa",
    "Sara",
    "Gemma"
]

barred_list = [
    "Wesley",
    "Steve",
    "Jessica",
    "Poppy",
    "Daisy"
]

def guest_allowed(name):
    if name in guest_list:
        return True
    else:
        return False

def guest_barred(name):
    if name in barred_list:
        return True
    else:
        return False


if guest_allowed(guest_name):
        print(f"You may enter {guest_name}!")
elif guest_barred(guest_name):
     print("Sorry but you cannot enter!")
else:
     print("sorry, but you will have to wait")


# def pin_checker(user_pin):
#     if user_pin == "1234":
#         return True
#     else:
#         return False
