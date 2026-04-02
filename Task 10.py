# Обчислення on-demand
def debug(x):
    print(f"Processing {x}")
    return x


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


def main():
    print("=== Створення pipeline ===")

    gen = pipeline(
        range(1, 10),
        [
            lambda xs: lazy_filter(lambda x: x % 2 == 0, xs),
            lambda xs: lazy_map(debug, xs),
            lambda xs: lazy_map(lambda x: x * x, xs)
        ]
    )

    print("Pipeline створено (ще нічого не обчислено)\n")

    print("=== Обчислення через next() ===")

    print(next(gen))  # 2 - debug - 4
    print(next(gen))  # 4 - debug - 16
    print(next(gen))  # 6 - debug - 36

    print("\n=== Подальша ітерація ===")

    for x in gen:
        print(x)


if __name__ == "__main__":
    main()