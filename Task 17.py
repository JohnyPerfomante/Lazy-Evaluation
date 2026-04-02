# Lazy reduce
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


def main():
    data = range(1, 6)  # 1, 2, 3, 4, 5

    print("Lazy reduce сумування:")
    gen = lazy_reduce(lambda a, b: a + b, data)

    print("Обчислюємо по одному елементу:")
    print(next(gen))  # 1 + 2 = 3
    print(next(gen))  # 3 + 3 = 6
    print(next(gen))  # 6 + 4 = 10
    print(next(gen))  # 10 + 5 = 15

    print("\nПовна ітерація:")
    for result in lazy_reduce(lambda a, b: a * b, range(1, 6)):
        print(result)


if __name__ == "__main__":
    main()