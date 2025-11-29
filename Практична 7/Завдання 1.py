about_me = {
    "Ім'я": "Роман",
    "Прізвище": "Римарук",
    "Вік": 18,
    "Дата народження": "01.12.2007",
    "Місце проживання": "Івано-Франківськ"
}

key_list = list(about_me.keys())

value_list = list(about_me.values())

item_list = list(about_me.items())

print("Словник about_me:", about_me)
print("-" * 30)
print("Список ключів (key_list):", key_list)
print("Список значень (value_list):", value_list)
print("Список пар ключ-значення (item_list):", item_list)