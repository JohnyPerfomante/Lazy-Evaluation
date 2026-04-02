# Генератор з yield
def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# Перевірка:
for x in generate_numbers(5):
    print(x)