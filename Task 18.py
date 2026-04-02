# Lazy Data Processing Engine
def lazy_filter(func, data):
    for x in data:
        if func(x):
            yield x


def lazy_map(func, data):
    for x in data:
        yield func(x)


def lazy_reduce(func, data, initial=None):
    it = iter(data)
    if initial is None:
        try:
            accum = next(it)
        except StopIteration:
            return
    else:
        accum = initial

    for x in it:
        accum = func(accum, x)
        yield accum


def run_pipeline(data, steps):
    result = data
    for step in steps:
        result = step(result)
    return result 


def main():
    data = range(1, 1_000_000)

    # Lazy pipeline: парні - * 10 - sum перших 5
    pipeline_gen = run_pipeline(
        data,
        [
            lambda xs: lazy_filter(lambda x: x % 2 == 0, xs),
            lambda xs: lazy_map(lambda x: x * 10, xs)
        ]
    )

    from itertools import islice
    total = sum(islice(pipeline_gen, 5))
    print("Сума перших 5 оброблених елементів:", total)

    print("\nПерші 3 елементи через next():")
    pipeline_gen2 = run_pipeline(
        range(1, 20),
        [
            lambda xs: lazy_filter(lambda x: x % 3 == 0, xs),
            lambda xs: lazy_map(lambda x: x * 2, xs)
        ]
    )

    print(next(pipeline_gen2))
    print(next(pipeline_gen2))
    print(next(pipeline_gen2))


if __name__ == "__main__":
    main()