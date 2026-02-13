# бей ближнего сри на нижнего

# Тип данних - характеристика данних що обозначає діапазон значень то набір операцій
"""
collection = list() # Функція коструктор
collection = []

print(type(collection)) # Класс list

items = [10, 12.3, "text", True] # погана практика

fruits = ["avocado", "apple", "orange", "lemon", "pear", "pamelo"]

fruits_tuple = tuple(fruits)

print(fruits_tuple)
print(type(fruits_tuple))

# fruits_tuple[3] = "kiwi"
print(fruits_tuple)
"""
colors = ("red", "green", "blue", "pink")
(red, green, blue, pink) = colors
print(red)
print(green)
print(blue)
print(pink)

(red, green, *other_colors) = colors
print(red)
print(green)
print(*other_colors)

"""
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
#fruits.clear()
print(", ".join(fruits))
print(len(fruits))

#apple_count = fruits.count("apple")
#print(apple_count)
#mango = fruits.count("mango")
#print(mango)
#banana_count = fruits.count("banana")
#print(banana_count)


# pamelo_index = fruits.index("pamelo")
# print(pamelo_index)

#apple_index = fruits.index("apple")
#print(apple_index)

# banana_index = fruits.index("banana")

fruits_copy = fruits.copy()
fruits_copy.append("orange")
print(fruits_copy)
print(fruits)

fruits.reverse()
print(fruits)

"""
"""

number = [10, 3, -5, 0, 0, -10, 12, 1]

even_numbers = [x for x in number if x % 2 == 0]
print(even_numbers)

odd_numbers = [x for x in range(1, 20, 2)]
print(odd_numbers)

list2d = [
    [1, 2, 3]
    [4, 5, 6]
]
print(list2d[0])
print(list2d[0][1])
"""
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