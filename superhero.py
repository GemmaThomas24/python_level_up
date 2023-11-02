class Superhero():
    def __init__(self, superhero_name, superhero_identity, superhero_superpower, superhero_enemy):
        self.name = superhero_name
        self.identity = superhero_identity
        self.superpower = superhero_superpower
        self.enemy = superhero_enemy
    
    def introduce_superhero(self):
        print((f"I am {self.name}, my real identity is {self.identity}. My superpower is {self.superpower} and my arch nemesis is {self.enemy}"))

# self- so we know which object we are referencing