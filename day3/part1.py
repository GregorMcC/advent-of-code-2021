from collections import Counter

from utils import load_file


def main() -> None:
    dataset = load_file()
    parsed_dataset = [''.join(x) for x in list(zip(*dataset))]
    gamma_rate = int(''.join([Counter(y).most_common()[0][0] for y in parsed_dataset]), 2)
    epsilon_rate = int(''.join([Counter(y).most_common()[-1][0] for y in parsed_dataset]), 2)

    print(gamma_rate * epsilon_rate)


if __name__ == "__main__":
    main()
