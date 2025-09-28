password = input("Введіть пароль: ")

passcheck = len(password)

if passcheck <= 4:
    print("Пароль закороткий")
elif passcheck >= 10:
    print("Пароль задовгий")
else:
    print("Прийнято")