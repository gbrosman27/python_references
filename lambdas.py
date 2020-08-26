# map iterates over an iterable and can be converted into something new like a list.
names = ["Kobe", "Chelsea", "Greg", "Kelci", "Dan"]

names2 = list(map(lambda x: x.upper(), names))

print(names2)

# filters out values of a list that you specify.
names_filtered = list(filter(lambda n: n[0] == "K", names))

print(names_filtered)

# Finds the name that is the longest in the list.
names_max = max(names, key=lambda n: len(n))

print(names_max)


# For arguments passed in, if even, add them together and return. Used generator expression.
def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)


# For arguments passed in, if type is a float, add them together and return. Used generator expression.
def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)
