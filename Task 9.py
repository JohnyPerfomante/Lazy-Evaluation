# Відкладене виконання

# Вихідна функція
def debug(x):
    print(f"Processing {x}")
    return x

# Lazy pipline
def lazy_map(func, data):
    for x in data:
        yield func(x)

def pipeline(data, steps):
    result = data
    for step in steps:
        result = step(result)
    return result


result = pipeline(
    range(1, 5),
    [
        lambda xs: lazy_map(debug, xs),   # debug в pipeline
        lambda xs: lazy_map(lambda x: x * x, xs)
    ]
)