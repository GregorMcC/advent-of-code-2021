from utils import load_file


def _add(a: int, b: int) -> int:
    return a + b


def _mul(a: int, b: int) -> int:
    return a * b


def _sub(a: int, b: int) -> int:
    return a - b


ACTIONS = {"down": (_add, _add), "forward": (_add, _mul), "up": (_sub, _sub)}
HORIZONTAL_ACTIONS = ["forward"]
DEPTH_ACTIONS = ["down", "up"]


def main() -> None:
    dataset = load_file()

    aim = 0
    depth = 0
    horizontal = 0

    for action, amount in dataset:
        if action in HORIZONTAL_ACTIONS:
            horizontal = ACTIONS[action][0](horizontal, amount)
            depth = ACTIONS[action][0](depth, ACTIONS[action][1](aim, amount))
        elif action in DEPTH_ACTIONS:
            aim = ACTIONS[action][1](aim, amount)

    print(depth * horizontal)


if __name__ == "__main__":
    main()
