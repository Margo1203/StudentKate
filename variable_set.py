s = {"Катя", "Калинина", "Катя"}
print(s)

#получение длины строки 2 или 3 лемента?
s = {"Катя", "Калинина", "Катя"}
print(len(s))

#назанчение через команду set
users = set()
users.add("Катя","Калинина")
print(s)

#пересечение множеств
s = {"Катя", "Калинина", "Леонидовна"}
s1 = {"Катя", "Калинина"}
s2 = s.intersection(s1)
print(s2)

#объединение множеств

s = {"Катя", "Калинина", "Леонидовна"}
s1 = {"Катя", "Калинина"}
s2 = s.union(s1)
print(s2)

#Разность множеств
s = {"Катя", "Калинина", "Леонидовна"}
s1 = {"Катя", "Калинина"}
s2 = s.difference(s1)
print(s2)


#определение подмножества
s = {"Катя", "Калинина", "Леонидовна"}
s1 = {"Катя", "Калинина"}
print(s.issubset(s1))






