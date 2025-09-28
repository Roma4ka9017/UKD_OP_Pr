a = float(input("Введіть перше число: "))
op = input("Введіть оператор (+, -, /, *, **): ")
b = float(input("Введіть друге число: "))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b
elif op == "**":
    result = a ** b

print("Результат:", result)