def colorize(text, color):
    """Shows error handling if the arguments passed in are not valid strings."""
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")


colorize([], 'cyan')


# colorize(34, "red")

# Uses error handling to catch if 2 integers are not passed in, or if the second integer is a zero.
def divide(num1, num2):
    try:
        total = num1 / num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total
