# Compose lazy functions
def compose(f, g):
    return lambda x: f(g(x))


def main():
    def multiply_by_2(x):
        print(f"multiply_by_2({x})")
        return x * 2

    def add_3(x):
        print(f"add_3({x})")
        return x + 3

    h = compose(add_3, multiply_by_2)

    print("Результати композиції для 1..5:")
    for i in range(1, 6):
        print(h(i))


if __name__ == "__main__":
    main()