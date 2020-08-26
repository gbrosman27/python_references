# The class to represent an Animal. Pets will inherit from this class.
class Animal:
    def __init__(self, name, age, gender, species):
        self.name = name
        self.age = age
        self.gender = gender
        self.species = species

    def __repr__(self):
        return f"{self.name}({self.age}), is a {self.gender} {self.species}."

    @staticmethod
    def speak(sounds):
        return print(sounds)
