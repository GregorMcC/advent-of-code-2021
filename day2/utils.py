def load_file() -> list[tuple[str, int]]:
    with open("input", "r") as file:
        dataset = [line.rstrip() for line in file]

    parsed_dataset = []
    for line in dataset:
        parts = line.split(" ")
        parsed_dataset.append((parts[0], int(parts[1])))

    return parsed_dataset
