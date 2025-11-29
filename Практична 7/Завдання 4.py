words = {
    "apple": "яблуко",
    "cow": "корова",
    "orange": "апельсин",
    "hello": "привіт",
    "Monday": "Понеділок",
    "dog": "пес"
}

user_input = input("Введіть слово для перекладу (латиницею): ").lower()

translation = words.get(user_input, "unknown")

print(f"Ваше слово: {user_input}")
print(f"Переклад: {translation}")