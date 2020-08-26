# Asks user for kilometers cycled and stores value
print("How many kilometers did you cycle today?")
kilometers = input()

# convert kilometers to miles
miles = float(kilometers) / 1.609

# round to 2 decimal places
miles = round(miles, 2)

# print using two different format techniques
print(f"You cycled {miles} miles today!")
print("{} is a good workout!".format(miles))
