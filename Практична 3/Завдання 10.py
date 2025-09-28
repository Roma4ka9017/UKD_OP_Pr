text = "qwertyagentbondqazwsx"

start = text.find("agent")
end = text.find("bond")
name = text[start:end]
surname = text[end:end+4]

print(name.capitalize(), surname.capitalize())