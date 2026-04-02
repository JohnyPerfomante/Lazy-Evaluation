# Pipeline
def pipeline(data, steps):
    result = data
    for step in steps:
        result = step(result)
    return result

# Використання:
def lazy_filter(func):
    return lambda data: (x for x in data if func(x))

def lazy_map(func):
    return lambda data: (func(x) for x in data)


data = range(1, 10)

result = pipeline(
    data,
    [
        lazy_filter(lambda x: x % 2 == 0),
        lazy_map(lambda x: x * x)
    ]
)

for x in result:
    print(x)