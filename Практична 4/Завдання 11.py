password = input("Введіть пароль: ")

if len(password) >= 8:
    has_digit = any(ch.isdigit() for ch in password)
    has_alpha = any(ch.isalpha() for ch in password)

    if has_digit and has_alpha:
        print("Надійний пароль")
    else:
        print("Додай цифру!")
else:
    print("Закороткий пароль")