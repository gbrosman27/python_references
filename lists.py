answer1 = [letters for letters in "amazing" if letters not in "aeiou"]
print(answer1)

answer2 = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]
print(answer2)

answer3 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
print(answer3)

answer4 = [[val for val in range(0, 10)] for numbers in range(0, 4)]
print(answer4)

answer5 = [[i for i in range(0, 3)] for num in range(0, 3)]
print(answer5)


