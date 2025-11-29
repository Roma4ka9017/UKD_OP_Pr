user = {"login": "admin", "password": "1234587", "email": "mamkin.odmen@ukrtele.com"}

print(f"Початковий словник: {user}")

if "email" in user:
    # 3. Якщо присутній, вивести його значення
    print(f"ВО!!! Ключ 'email' присутній. Значення: {user['email']}")
else:
    # 4. Якщо ні, додати цей ключ та значення
    user["email"] = "admin@gmail.com"
    print("ЙОЙ-ЙОЙ-ЙОЙ, АЛЕ СВАРИТЬСЯ!!! Ключ 'email' був відсутній і доданий.")
    print(f"Оновлений словник: {user}")