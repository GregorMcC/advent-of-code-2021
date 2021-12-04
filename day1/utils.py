def load_file() -> list[int]:
    with open("input", "r") as file:
        dataset = [int(line.rstrip()) for line in file]

    return dataset
