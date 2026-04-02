# Читання файлу (імітація)
def read_lines():
    lines = [
        "First line",
        "Second line",
        "Third line",
        "Fourth line"
    ]

    for line in lines:
        print(f"Reading: {line}")  # Момент читання
        yield line


def main():
    print("=== Створення генератора ===")
    gen = read_lines()

    print("Генератор створено (файл ще не читається)\n")

    print("=== Читання через next() ===")
    print(next(gen))
    print(next(gen))

    print("\n=== Читання через for ===")
    for line in gen:
        print(line)


if __name__ == "__main__":
    main()