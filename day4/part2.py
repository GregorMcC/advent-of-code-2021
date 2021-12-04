from utils import load_file


def _chunk(lst: list, chunks: int) -> list[list]:
    for i in range(0, len(lst), chunks):
        yield lst[i : i + chunks]


def _check_winner(
    board: list[list], numbers_drawn: list
) -> tuple[list[list], list[int]]:
    # check rows
    for row in board:
        if all(value in numbers_drawn for value in row):
            return board, numbers_drawn
    for column in list(zip(*board)):
        if all(value in numbers_drawn for value in column):
            return board, numbers_drawn


def _calculate_final_score(winning_board, numbers_drawn) -> int:
    uncalled_numbers = []
    for row in winning_board:
        for value in row:
            if value not in numbers_drawn:
                uncalled_numbers.append(value)

    return sum(uncalled_numbers) * numbers_drawn[-1]


def main() -> None:
    data = load_file("input")

    numbers_to_draw = [int(num) for num in data[0].split(",")]
    rows = []
    for row in data[1:]:
        rows.append([int(val) for val in row.split()])

    boards = list(_chunk(rows, 5))

    winning_board = None
    numbers_drawn = None
    winning_boards = []
    try:
        for counter in range(len(numbers_to_draw)):
            for board in boards:
                if winner := _check_winner(
                    board=board, numbers_drawn=numbers_to_draw[:counter]
                ):
                    winning_board, numbers_drawn = winner
                    if winning_board not in winning_boards:
                        winning_boards.append(winning_board)
                    if len(winning_boards) == len(boards):
                        raise StopIteration
    except StopIteration:
        pass

    print(
        _calculate_final_score(
            winning_board=winning_boards[-1], numbers_drawn=numbers_drawn
        )
    )


if __name__ == "__main__":
    main()
