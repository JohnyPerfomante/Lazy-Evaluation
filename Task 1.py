# Порівняння eager vs lazy
data = [1, 2, 3, 4, 5]

# eager
squares_list = [x * x for x in data]

# lazy
squares_gen = (x * x for x in data)

# Перевірка
print(type(squares_list))
print(type(squares_gen))

# Ітерація:
print("List:")
for x in squares_list:
    print(x)

print("Generator:")
for x in squares_gen:
    print(x)

# Коли обчислюється значення? Обчислення відбувається одразу при створенні, весь список вже готовий у пам’яті:
squares_list = [x * x for x in data]

# Яка різниця у пам’яті? List: Зберігає всі елементи одразу.
# Generator: Зберігає поточний стан ітерації, одне значення за раз.

# Демонстрація різниці:
squares_gen = (x * x for x in data)

print(next(squares_gen))  # 1
print(next(squares_gen))  # 4