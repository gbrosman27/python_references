# The class to represent a Dog.
from Inheritance.Animal import Animal


class Dog(Animal):
    def __init__(self, name, favorite_toy, age, gender, species, fur_color):
        super().__init__(name, age, gender, species)
        self.favorite_toy = favorite_toy
        self.fur_color = fur_color


# Instantiate an instance of Kobe the dog.
kobe = Dog("Kobe", 7, "male", "rottweiler", "brown")

dog_toys = ["kong", "ball", "bone", "chicken"]
for toy in dog_toys:
    if "chicken" in dog_toys:
        kobe.favorite_toy = toy

print(kobe)
print(f"Kobe's favorite toy is {kobe.favorite_toy}.")

# Kobe speaks via the speak function from Animal (inherited).
kobe.speak("Bark, bark, woof, roo!")


# Check if inheritance is True.
print(issubclass(Dog, Animal))