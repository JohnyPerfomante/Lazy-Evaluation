# Логування pipeline
def debug(x, stage=""):
    print(f"[DEBUG] {stage}: Processing {x}")
    return x


def lazy_filter(func, data, stage=""):
    for x in data:
        if func(x):
            yield debug(x, stage)


def lazy_map(func, data, stage=""):
    for x in data:
        yield debug(func(x), stage)


def pipeline(data, steps):
    result = data
    for step in steps:
        result = step(result)
    return result


def main():
    transactions = range(1_000_000)

    # Lazy pipeline з debug
    result_gen = pipeline(
        transactions,
        [
            lambda xs: lazy_filter(lambda x: x % 2 == 0, xs, stage="Filter even"),
            lambda xs: lazy_map(lambda x: x * 10, xs, stage="Multiply by 10")
        ]
    )

    total = 0
    for i, x in enumerate(result_gen):
        total += x
        if i == 9:  # Лише перші 10
            break

    print("\nСума перших 10 оброблених транзакцій:", total)


if __name__ == "__main__":
    main()