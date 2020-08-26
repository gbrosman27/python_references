class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f"{self.first} is {self.age} years old."

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def favorite_sport(self, sport):
        return f"{self.first}'s favorite sport is {sport}."

    def is_an_adult(self, age):
        if self.age > 18:
            return f"{self.full_name()} is {self.age} years old and is an adult."
        return f"{self.full_name()} is not an adult."

    def birthday(self):
        self.age += 1
        return f"Happy {self.age} Birthday {self.first}"


# Create a Moderator class that inherits from Users.
class Moderator(User):
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community."


user1 = User("Greg", "Brosman", 32)
user2 = User("Chelsea", "Brosman", 31)
jasmine = Moderator("Jasmine", "O'Connor", 47, "Piano")

print(user1.full_name())
print(user2.initials())
print(user2.favorite_sport("swimming"))
print(user2.is_an_adult(31))
print(user1.birthday())
print(user1.age)
print(User.display_active_users())
print(user1)
print(jasmine.full_name())
print(jasmine.community)
print(jasmine.remove_post())