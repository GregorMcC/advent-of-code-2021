from utils import load_file


def _add(a: int, b: int) -> int:
    return a + b


def _sub(a: int, b: int) -> int:
    return a - b


ACTIONS = {
    "down": _add,
    "forward": _add,
    "up": _sub
}
HORIZONTAL_ACTIONS = ["forward"]
DEPTH_ACTIONS = ["down", "up"]


def main() -> None:
    dataset = load_file()

    depth = 0
    horizontal = 0

    for action, amount in dataset:
        if action in HORIZONTAL_ACTIONS:
            horizontal = ACTIONS[action](horizontal, amount)
        elif action in DEPTH_ACTIONS:
            depth = ACTIONS[action](depth, amount)

    print(depth * horizontal)


if __name__ == "__main__":
    main()
