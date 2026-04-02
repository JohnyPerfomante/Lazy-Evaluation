# Lazy квадрат
def lazy_square(data):
    for x in data:
        yield x * x

# Перевірка:
data = [1, 2, 3, 4, 5]

gen = lazy_square(data)

print(type(gen))

for x in gen:
    print(x)