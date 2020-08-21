s = ("Катя", 31)
print(s)

# один элемент, надо ставить запятую
s = ("Катя",)

# использование функции tuple

s_list = ["Катя", "Калинина"]
s_tuple = tuple(s_list)
print((s_tuple))

# обращение к элементу

s = (1, 2, "Cat", 5)
print(s[2])

# разложение кортежа на переменные

s = ("Катя", "Калинина", "31")
name, surname, age = s
print(name)
print(surname)
print(age)

# длина кортежа
s = (1, 2, "Катя", 7, 9, "Калинина")
print(len(s))
