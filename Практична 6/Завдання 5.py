numbers = (1, 2, 3, 4, 5, -5, 12, 5, 42, 34)

numbers_list = list(numbers)
numbers_list.append(-56)
numbers = tuple(numbers_list)
print(numbers)

numbers_list = list(numbers)
numbers_list.remove(5)
numbers = tuple(numbers_list)
print(numbers)
