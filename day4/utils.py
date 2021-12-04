def load_file(name: str) -> list[str]:
    with open(name, 'r') as file:
        dataset = [line.rstrip() for line in file if line != "\n"]
    
    return dataset
