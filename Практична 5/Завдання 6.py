num1 = [1, 5, -4, 10, 2, 2, 3.4, -4]
num2 = [3, -6, -7, -89, 90, 2]

num1.extend(num2)
print("Об’єднаний список:", num1)

num1.sort()
print("Сортування за зростанням:", num1)

num1.sort(reverse=True)
print("Сортування за спаданням:", num1)