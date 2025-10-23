fruits1 = ("apple", "orange", "banana", "pineapple", "cgerrys")
fruits2 = ("mango", "orange", "lemon", "", "pear")
num = (1, -6, 23, 45)

fruits3 = fruits1 + fruits2
print(fruits3)

num_multiplied = num * 3
print(num_multiplied)

first, *all_others, second_to_last, last = num
print(first)
print(all_others)
print(second_to_last)
print(last)
