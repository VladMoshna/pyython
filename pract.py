# zavd 1
numbers = input("Введіть числа через пробіл: ").split()

total = 0

for i in range(len(numbers)):
    total += int(numbers[i])

average = total / len(numbers)

print("Сума:", total)
print("Середнє арифметичне:", average)


# zavd 2
numbers = input("Введіть числа через пробіл: ").split()
x = int(input("Введіть число для пошуку: "))

count = 0

for i in range(len(numbers)):
    if int(numbers[i]) == x:
        count += 1

print("Кількість входжень:", count)


# zavd 3
numbers = input("Введіть числа через пробіл: ").split()

sum_positive = 0

for i in range(len(numbers)):
    if int(numbers[i]) > 0:
        sum_positive += int(numbers[i])

print("Сума додатних чисел:", sum_positive)


# zavd 4
numbers = input("Введіть числа через пробіл: ").split()

print("Індекси парних чисел:")

for i in range(len(numbers)):
    if int(numbers[i]) % 2 == 0:
        print(i)


# zavd 5
numbers = input("Введіть числа через пробіл: ").split()

unique = []

for i in range(len(numbers)):
    if numbers[i] not in unique:
        unique.append(numbers[i])

print("Унікальні елементи:", unique)