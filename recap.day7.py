# Class Method
# Blueprint to make lots of objects. Names Pascal case
# def __init__(self) initilizer (set parameter of 'self')
# e.g superhero activity

# food_menu = {
#   "Croissant": 150,
#   "Muffin": 210, 
#   "Toast": 100,
#   "Panini": 290,
#   "Buttered Roll": 70,
#   "Stroopwafel": 50
# }


# food_order = [
  
# ]
  
  


# answer = input("Would you like to order food?").capitalize()

# while answer == "Yes":
#   print(food_menu)
#   food_item = input("Food choice  >  ")
#   if food_item in food_menu:
#     quantity = int(input("How many do you want?"))
#     food_order.append(food_item*quantity)
#     food_value = food_menu.get(food_item)
#     food_order.append(food_value*quantity)
#     print(food_order)
#     answer = input("Would you like to order more food?").capitalize()
#   else:
#     print("Sorry we don't have that item. Try again")

# else:
#   print("checkout")


# total_cost = 0

# for i in food_order:
#   total_cost = sum(food_order(food_item))



# drink_menu = {
#     "Tea" : 1.00,
#     "Americano" : 1.70,
#     "Latte" : 1.90,
#     "Cappuccino" : 1.90,
#     "Mocha":2.00,
# }
# drink_order = []
# total_cost = 0

# drink_answer = input("Would you like to order a drink?").capitalize()

# while drink_answer == "Yes":
#     print(drink_menu)
#     drink_item = input("Drink choice: ")
#     if drink_item in drink_menu:
#         quantity = int(input("How many do you want?"))
#         drink_order.append((drink_item, quantity))
#         drink_value = drink_menu.get(drink_item)
#         cost = drink_value * quantity
#         total_cost += cost
#         print(f"You have ordered {quantity} x {drink_item}. The total cost is £{total_cost}")
#         drink_answer = input("Would you like to order a drink?").capitalize()
#     else:
#         print("Sorry we don't have that item. Try again")

# else:
#     print("Checkout")


# for i, cost in order:
#     total_cost += cost
#     print(f" Your bill comes to: {total_cost}")

# total_cost = (drink_cost + food_cost)


# print("****** RECIEPT******")
# print(order_number)
# print(order)
# print("Your bill comes to {total_cost}")


# order_list = []

# for item in order_list:
#     print(item)

# counter = 0



# drink_menu = {
#       "Tea" : 1.00,
#       "Americano" : 1.70,
#       "Latte" : 1.90,
#       "Cappuccino" : 1.90,
#       "Mocha":2.00,
#   }

# food_menu = {
#     "Croissant": 1.50,
#     "Muffin": 2.10, 
#     "Toast": 1.00,
#     "Panini": 2.90,
#     "Buttered Roll": .70,
#     "Stroopwafel": .50
#   }


# while True:


#   order = []

#   total_cost = 0



#   drink_answer = input("Would you like to order a drink?  ").capitalize()

#   while drink_answer == "Yes":
#         print(drink_menu)
#         drink_item = input("Drink choice: ").capitalize()
#         if drink_item in drink_menu:
#            drink_quantity = int(input("How many do you want? "))
#            order.append((drink_quantity, drink_item))
#            drink_value = drink_menu.get(drink_item)
#            drink_cost = drink_value * drink_quantity
#            drink_rounded_cost = round(drink_cost, 2)
#            total_cost += drink_rounded_cost
#            print(f"You have now ordered {order}. The total cost is £{total_cost}")
#            drink_answer = input("Would you like to order another drink? ").capitalize()
#         else:
#             print("Sorry we don't have that item. Try again")
  
#   food_answer = input("Would you like to order food? ").capitalize()
  
#   while food_answer == "Yes":
#         print(food_menu)
#         food_item = input("Food choice: ").capitalize()
#         if food_item in food_menu:
#            food_quantity = int(input("How many do you want? "))
#            order.append((food_quantity, food_item))
#            food_value = food_menu.get(food_item)
#            food_cost = food_value * food_quantity
#            rounded_food_cost = round(food_cost, 2)
#            total_cost += rounded_food_cost
#            print(f"You have ordered {food_quantity} x {food_item}. The total cost so far is £ {total_cost}")
#            food_answer = input("Would you like to order some more food? ").capitalize()
#         else:
#             print("Sorry we don't have that item. Try again")
  
#   print("Checkout")

#     for item in order:
#       print(item)

  
#   print(f"£{total_cost}")
#   print("***** RECEIPT *****")
#   print(f"Your bill comes to £{total_cost}")
#   counter += 1
#   print(f"Your order number is {counter}")

 
#   for item in order:
#     print(item)

counter = 0

import datetime







drink_menu = {
      "Tea" : 1.00,
      "Americano" : 1.70,
      "Latte" : 1.90,
      "Cappuccino" : 1.90,
      "Mocha": 2.00,
  }

food_menu = {
    "Croissant": 1.50,
    "Muffin": 2.10, 
    "Toast": 1.00,
    "Panini": 2.90,
    "Buttered Roll": 0.70,
    "Stroopwafel": 0.50
  }


while True:


  order = [
    
  ]

  total_cost = 0

  user_name = input("Hello, what is your name? ")
  
  

  drink_answer = input("Would you like to order a drink?  ").capitalize()

  while drink_answer == "Yes":
      for k, v in drink_menu.items():
          print(f"{k} - £{v:.2f}")
      drink_item = input("Drink choice: ").capitalize()
      if drink_item in drink_menu:
           drink_quantity = int(input("How many do you want? "))
           order.append((drink_quantity, drink_item))
           drink_value = drink_menu.get(drink_item)
           drink_cost = drink_value * drink_quantity
           drink_rounded_cost = round(drink_cost, 3)
           total_cost += drink_rounded_cost
           drink_answer = input("Would you like to order another drink? ").capitalize()
      else:
            print("Sorry we don't have that item. Try again")

  for item in order:
     print(f" You have now ordered {item[0]} {item[1]}") 
  
  print(f"Your total cost is £ {total_cost:.2f}")
  food_answer = input("Would you like to order food? ").capitalize()
  
  while food_answer == "Yes":
      for k, v in food_menu.items():
          print(f"{k} - £{v:.2f}")
      food_item = input("Food choice: ").capitalize()
      if food_item in food_menu:
           food_quantity = int(input("How many do you want? "))
           order.append((food_quantity, food_item))
           food_value = food_menu.get(food_item)
           food_cost = food_value * food_quantity
           rounded_food_cost = round(food_cost, 3)
           total_cost += rounded_food_cost
           food_answer = input("Would you like to order some more food? ").capitalize()
      else:
            print("Sorry we don't have that item. Try again")
  for item in order: 
      print(f"You have now ordered {item[0]} {item[1]}")

  print(f"Your total cost is £ {total_cost:.2f}")
  print("Checkout")
  
  for item in order:
    print(f"{item[0]} {item[1]}")
    

  print(f"£{total_cost:.2f}")


# checkout_review = input("Is this order correct?").capitalize()

# while checkout_review != "Yes":
#         print("Please start your order again.")
#         order = [

#         ]


#         #.....

# else:
  print(f"Thank you {user_name} for shopping with us. Please insert your card.")
  print("Here is your receipt")
  print("***** RECEIPT *****")
  date_time = datetime.datetime.now()
  print(date_time)
  for item in order:
    print(f"{item[0]} {item[1]}")
  print(f"Your bill comes to £{total_cost:.2f}")
  counter += 1
  print(f"Your order number is {counter}")

  f = open("record.txt", "a")
  f.write(f"Name : {user_name}, Order : {counter}, Total : £{total_cost: .2f}, Date and Time : {date_time}\n")
  f.close()