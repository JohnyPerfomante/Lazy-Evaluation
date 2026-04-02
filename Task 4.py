# Lazy filter
def lazy_filter(func, data):
    for x in data:
        if func(x):
            yield x

# Перевірка:
data = [1, 2, 3, 4, 5]

def is_even(x):
    return x % 2 == 0

gen = lazy_filter(is_even, data)

print(type(gen))  # <class 'generator'>

for x in gen:
    print(x)