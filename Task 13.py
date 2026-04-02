# Обробка транзакцій (DE стиль)
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
    transactions = range(1_000_000)  # DE-style

    result_gen = pipeline(
        transactions,
        [
            lambda xs: lazy_filter(lambda x: x % 2 == 0, xs),
            lambda xs: lazy_map(lambda x: x * 10, xs)
        ]
    )

    total = 0
    for i, x in enumerate(result_gen):
        total += x
        if i == 99:  # Тільки перші 100
            break

    print("Сума перших 100 оброблених транзакцій:", total)


if __name__ == "__main__":
    main()