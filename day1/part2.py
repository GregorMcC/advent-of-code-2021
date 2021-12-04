from utils import load_file


def main() -> None:
    dataset = load_file()
    window_size = 3

    base = sum(dataset[:window_size])
    total_increasing = 0
    for i in range(len(dataset) - window_size + 1):
        summed_window = sum(dataset[i + 1 : i + window_size + 1])
        if summed_window > base:
            total_increasing += 1
        base = summed_window

    print(total_increasing)


if __name__ == "__main__":
    main()
