prices = {'apple': 50, 'banana': 20, 'cherry': 75}

most_expensive_item = max(prices, key=prices.get)

max_price = prices[most_expensive_item]

print(f"Словник цін: {prices}")
print(f"Товар з максимальною ціною: {most_expensive_item}")
print(f"Максимальна ціна: {max_price}")