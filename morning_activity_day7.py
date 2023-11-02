# Write a function whoch allows a user to give 2 intergers.
# Generate 6 random numbers between the values and sort them in order highest to lowest
# print numbers in this order
import random

print("Please enter 2 different numbers")

num_list = []

def rand_num(start, stop):
    for i in range(6):
        rand_num = random.randint(start,stop)
        num_list.append(rand_num)
        num_list.sort(reverse=True)
    print(num_list)

rand_num(int(input(" Number 1:   >   ")),int(input("Number 2:   >   ")))

# think i've done it where it prints 1 random number between 2 and 10


