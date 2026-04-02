# Генерація нескінченної послідовності
def infinite_numbers():
    n = 1
    while True:   # Нескінченний цикл
        yield n
        n += 1


def main():
    gen = infinite_numbers()

    print("Перші 10 чисел з нескінченної послідовності ():")
    for _ in range(10):
        print(next(gen))


if __name__ == "__main__":
    main()