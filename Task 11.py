# Великий діапазон
def lazy_map(func, data):
    for x in data:
        yield func(x)


def main():
    data = range(10**9)  # lazy iterable

    gen = lazy_map(lambda x: x * x, data)

    print("Перші 10 елементів:")

    count = 0
    for x in gen:
        print(x)
        count += 1
        if count == 10:
            break


if __name__ == "__main__":
    main()