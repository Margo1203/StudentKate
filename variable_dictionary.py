s = {1: "Катя", 2: "Калинина"}
s1 = dict(s)
print(s1)

# удаление элементов
phone = {"123456": "Катя", "987654": "Иван", "6548965": "Сергей"}
del phone["987654"]
print(phone)

# возвращение элемента по ключу

phone = {"123456": "Катя", "987654": "Иван", "6548965": "Сергей"}
print(phone.get("6548965"))

# копирование словаря
s = {1: "Катя", 2: "Калинина", 3: "Леонидовна"}
s1 = s.copy()
print(s1)

# Объединение словаря
s = {1: "Катя", 2: "Калинина", 3: "Леонидовна"}
s1 = {4: "31", 5: "Рязань"}
s.update(s1)

# Что будет тут?
s = {1: "Катя", 2: "Калинина", 3: "Леонидовна"}
s1 = {3: "31", 4: "Рязань"}
s.update(s1)
