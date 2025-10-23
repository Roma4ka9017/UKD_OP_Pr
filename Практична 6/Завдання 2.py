num1 = {1, 13, 3, 6, 7, 5, 4, 18}
num2 = {14, 3, 7, 11, 12, 9, 1}
num3 = {14, 3, 4, 21, 9, 18, 17, 2}

union_sets = num1 | num2 | num3
print(union_sets)

intersection_sets = num1 & num2 & num3
print(intersection_sets)

difference_1_2 = num1 - num2
print(difference_1_2)

difference_1_3 = num1 - num3
print(difference_1_3)

difference_2_1_3 = num2 - num1 - num3
print(difference_2_1_3)

symmetric_difference_sets = num1 ^ num2 ^ num3
print(symmetric_difference_sets)

num4 = {3, 4, 9}

is_num2_subset_num3 = num2.issubset(num3)
print(is_num2_subset_num3)

is_num4_subset_num3 = num4.issubset(num3)
print(is_num4_subset_num3)
