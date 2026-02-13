# бей ближнего сри на нижнего

# Тип данних - характеристика данних що обозначає діапазон значень то набір операцій

collection = list() # Функція коструктор
collection = []

print(type(collection)) # Класс list

items = [10, 12.3, "text", True] # погана практика

fruits = ["avocado", "apple", "orange", "lemon", "pear"]
print(", ".join(fruits))

fruits.append("pineapple")
print(", ".join(fruits))
fruits.extend(["mandarin", "grapefruit"])
print(", ".join(fruits))
fruits.insert(4, "mango")
print(", ".join(fruits))


fruits.pop(5)
print(", ".join(fruits))
fruits.remove("lemon")
print(", ".join(fruits))
fruits.clear()
print(", ".join(fruits))
print(len(fruits))



"""
print(fruits[0])
print(fruits[1])
print(fruits[1:3])
print(fruits[:3])
print(fruits[2:])
print(fruits[1:4:2])
print(fruits[::2])

print(fruits[-1])
print(fruits[-1:-3:-2])
print(fruits[::-2])


string = "text"
string[2] = "u"

fruits[1] = "mango"
print(fruits)

fruits_count = len(fruits)
print(fruits_count)

counter = 0
while counter < len(fruits):
    print(fruits[counter])
    counter += 1

for fruit in fruits:
    print(fruit)

names = input("Введіть список імен через кому: ")
print(type(names))
names = names.split(", ")
print(type(names))
print(names)
print(type(names))
print(", ".join(names))
print(type(names))
"""