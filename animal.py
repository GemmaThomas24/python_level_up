class Animal():
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    
    def eat(self):
            print(f"{self.name} is eating")
    
    def drink(self):
         print(f"{self.anme} is drinking")


class Parrots(Animal):
    def fly(self):
     print(f"{self.name} is flying")

class Fish(Animal):
      def swim(self):
          print(f"{self.name} is swimming")
     
