# template for our person object
# PascalCase- distince between a class and a function
# Person is the name of the class, implies I will make lots of people from it
# init(initilizing)
# every person that gets built will have own property
# object.property (self.name)
# Gemma object= Gemma.name
# which name of object you want to find
# class can have as mnay attributes as you need- age/height. Making a property of 'self' - 'This ones age, height'


class Person():
    
    def __init__(self, person_name, person_age, person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height
    
    def set_job(self, job_title):
         allowed_jobs = ["developer" "admin", "comliance", "instructor", "HR", "finance"]
         while job_title not in allowed_jobs:
              print("This is not a role within this company")
              print("Please enter your job again")
              job_title = input()
         self.job = job_title
    
    def get_age(self):
         return self.age

    def set_new_name(self, person_name):
            self.name = person_name
    
    def set_hair_colour(self, hair_colour):
         self.set_hair_colour = hair_colour
        #  set = setters = to be able to add more properties without amending the inital class structure

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} and I am {self.height} tall")
        # this one is a function

# setter allows you to add more properties to the person. But you have to meet the inital 3 arguments in the Person class.
# Classes should be Open to expansion. To be able to improve on them.



