from utils import load_file


def main() -> None:
    dataset = load_file()

    base = dataset[0]
    total_increasing = 0

    for measurement in dataset[1:]:
        if measurement > base:
            total_increasing += 1
        base = measurement
    print(total_increasing)


if __name__ == "__main__":
    main()
