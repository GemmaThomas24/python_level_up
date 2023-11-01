# EXTRA ACTIVITES Pt1
import random
# 1. Create a lottery number generator
# generate 6 random numbers between 1-50
# ensure number does not apprear more than once

# num_list = []
# # need a place to hold 6 numbers

# for i in range(6):
#     x = random.randint(0,51)
#     if x not in num_list:
#         num_list.append(x)
# # for i in range 6: this starts a loop that will run 6 times.
# # x = random.randint(0,51)- in each iteration, thus generates a random interger (x)between 0 and 50
# # if x not in num_list-checks if random number not already present. if True, will then add number to list (num_list.append(x)
# print(num_list)

# Activity 2
# create a number guessing game
# user has to say if next number generated will be higher or lower than current number
# user has only 3 guesses


# need random number generator 
# user input


# counter = 0


# while counter < 3:
#     rand_num = random.randint(0, 51)
#     print(rand_num)
#     guess = (input("Will the next number generated be higher or lower?  >  "))
#     rand_num2 = random.randint(0, 51)
#     print(rand_num2)

#     if guess == "higher" and rand_num2 > rand_num:
#         print("You guessed correctly!")
#     elif guess == "lower" and rand_num2 < rand_num:
#         print("You guessed correctly!")
#     else:
#         print("You guessed incorrectly!")
#         counter +=1
# print("Game Over")


# while True:
#     if guess < rand_num:
#         print("You guessed correctly!")
#     else:
#         print("You guessed incorrectly!")
#     guess = (input("Will the next number generated be higher or lower?  >  "))

#     if guess > rand_num:
#         print("You guessed correctly!")
#     else:
#         print("You guessed incorrectly!")
#     guess = (input("Will the next number generated be higher or lower?  >  "))

    # how to generate a number 1st before the question is asked 
    # how to display number in terminal?


# Activity 3
# create a quiz of five questions on any topic
# user gets 5 points for each correct answer and loses 2 points for each incorrect answer
# let the user answer all five questions and display total score at the end 


# counter = 0

# questions = [
#     ("Who stared in Titanic as Rose's love interest?", "Leonardo DiCaprio"),
#     ("What location were The Lord of the Rings movies filmed at?", "New Zealand"),
#     ("What Christmas film stars Hugh Grant as the UK Prime Minister?", "Love Actually"),
#     ("Who is the actor that stars as the main character in Mission Impossible?", "Tom Cruise"),
#     ("What movie has the famous line 'I'll be back'?", "The Terminator")
# ]

# for question, correct_answer in questions:
#     answer = input(f"{question}")
#     if answer == correct_answer.lower():
#         print("Correct!")
#         counter = counter+5
#     else:
#         print(f"The answer is {correct_answer}, not {answer}")
#         counter = counter-2

# print(counter)

# Activity 4
# create a function that checks if a specific film is in the list.
# if so, print a sucesses message
# if it's not in list, update the list
# if the is film Ghostbusters, add it at index positon 0

# for loop for items in list
# list with ghostbusters on it and merge 2 list together
# .append to add to list

# fav_films= [
#     "Jurassic Park",
#     "Spiderman",
#     "Shrek"
# ]

# ghostbusters = [
#     "Ghostbusters"
# ]

# def film_checker(name):
#     if name in fav_films:
#             print(f"Great! {name} is already on the list!")
#     elif name in ghostbusters:
#          fav_films.insert(0, name)
#          print(f" {name} has been added to the list!")
#     else:
#         fav_films.append(name)
#         print(f"This item was not on the list, {name} has been added!")

# film_checker("Ghostbusters")

# print(fav_films)

# Activity 5
# create a program which takes the user's input and if it's a number, turns to an interger.
# if the input is a string, make the string uppercase instead

# user_input = input("How old are you?  >  ")

# if user_input.isnumeric():
#     user_input = int(user_input)
# else:
#     user_input = user_input.upper()

# print(user_input)

# Activity 6
# import time
# # Create a hide and seek program
# # User needs to be able to enter their name and pick their hiding place from a list
# # programe should count out 10 seconds and try to find the user
# # program should be allowed 5 attempts to guess
# # look at time.sleep for pausing


# place = [
#     "kitchen",
#     "storing cupboard",
#     "bedroom",
#     "living room",
#     "bathroom",
#     "shed"
# ]

# user_name = input("What is your name?  >  ")
# user_hiding_place = input("From the list where you would like to hide?  >  ")

# counter = 0

# def hiding_place(user_name, user_hiding_place):
#     user_name = input("What is your name?  >  ")
#     user_hiding_place = input("From the list where you would like to hide?  >  ")
#     for i in place:
#         if place == user_hiding_place:
#             print(f" My name is {user_name} and I would like to hide in the {} ")




# for question, correct_answer in questions:
#     answer = input(f"{question}")
#     if answer == correct_answer.lower():
#         print("Correct!")
#         counter = counter+5
#     else:
#         print(f"The answer is {correct_answer}, not {answer}")
#         counter = counter-2

# print(counter)