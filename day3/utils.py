def load_file() -> list[str]:
    with open('input', 'r') as file:
        dataset = [line.rstrip() for line in file]

    return dataset
