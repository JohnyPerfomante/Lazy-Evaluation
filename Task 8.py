# Lazy pipeline
def lazy_filter(func, data):
    for x in data:
        if func(x):
            yield x

def lazy_map(func, data):
    for x in data:
        yield func(x)

def pipeline(data, steps):
    result = data
    for step in steps:
        result = step(result)
    return result


result = pipeline(
    range(1, 1_000_000),
    [
        lambda xs: lazy_filter(lambda x: x % 2 == 0, xs),
        lambda xs: lazy_map(lambda x: x * x, xs)
    ]
)

# Перші 5 значень
for i, x in enumerate(result):
    if i >= 5:
        break
    print(x)