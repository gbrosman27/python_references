# def generate_evens():
#     return [nums for nums in range(2, 50, 2)]
#
# print(generate_evens())


# def return_day(num):
#     days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     if 0 < num <= len(days):
#         return days[num-1]
#     return None


# def last_element(list_nums):
#     """Returns the last element in the list. If no list found, return none"""
#     if list_nums:
#         return list_nums[-1]
#     return None


# def contains_purple(*args):
#     if "purple" in args:
#         return True
#     return False
#
#
# print(contains_purple("orange", "purple"))


# def combine_words(word, **kwargs):
#     """Checks if kwargs contains a prefix or suffix then returns with the passed in word."""
#     if "prefix" in kwargs:
#         return kwargs["prefix"] + word
#     elif "suffix" in kwargs:
#         return word + kwargs["suffix"]
#     return word
#
#
# print(combine_words("child", prefix="man", suffix="dog"))

# def single_letter_count(word, letter):
#     """Counts the specified letter of the word passed in."""
#     return word.lower().count(letter.lower())
#
#
# print(single_letter_count("chelsea", "e"))

