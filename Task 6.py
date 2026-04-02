# Комбінування
def lazy_filter(func, data):
    for x in data:
        if func(x):
            yield x

def lazy_map(func, data):
    for x in data:
        yield func(x)


data = range(1, 10)

result = lazy_map(
    lambda x: x * x,
    lazy_filter(lambda x: x % 2 == 0, data)
)

for x in result:
    print(x)