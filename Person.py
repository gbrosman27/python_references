from Human import *
from Animal import *
from utils import age_in_days

# The class to represent Persons.
class Person(Human):
    def __init__(self, name, favorite_sport, age, gender, hair_color):
        super().__init__(name, age, gender, hair_color)
        self.favorite_sport = favorite_sport


chelsea = Person("Chelsea", "swimming", 31, "female", "brown",)
print(chelsea)
chelsea.talk()
chelsea.walk()
chelsea.age = age_in_days(30)
print(f"Age in days: {chelsea.age}")

greg = Person("Greg", "Lacrosse", 32, "male", "brown")
print(greg)
greg.talk()
