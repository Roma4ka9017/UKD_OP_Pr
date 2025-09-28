grade = input("Введіть оцінку: ")

if grade == "A":
    print("5")
elif grade == "B":
    print("4")
elif grade == "C":
    print("3")
elif grade == "D":
    print("2")
elif grade == "E":
    print("1")
elif grade == "F":  #
    print("0")      # А як я маю зробити це завдання якщо букв 6, а балів 5? Ну окей, зроблю по свому
else:
    print("Не оцінка")