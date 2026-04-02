# Lazy map
def lazy_map(func, data):
    for x in data:
        yield func(x)

# Перевірка:
data = [1, 2, 3, 4, 5]

gen = lazy_map(lambda x: x * x, data)

print(type(gen))  # <class 'generator'>

for x in gen:
    print(x)