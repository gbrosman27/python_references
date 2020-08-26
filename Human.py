# The class to represent a Human. People will inherit from this class.
class Human:
    def __init__(self, name, age, gender, hair_color):
        self.name = name
        self.age = age
        self.gender = gender
        self.hair_color = hair_color

    def __repr__(self):
        return f"{self.name}({self.age}), is a {self.gender} with {self.hair_color} colored hair."

    def talk(self):
        print(f"Hi, my name is {self.name}!")

    def walk(self):
        print("I think I will take a walk.")


