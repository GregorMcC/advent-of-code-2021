import re

from dataclasses import dataclass

from utils import load_file


@dataclass
class Coord:
    x: int
    y: int


def main() -> None:
    dataset = load_file("input")
    coord_regex = re.compile("\d+,\d+")
    coord_pairs = [re.findall(coord_regex, line) for line in dataset]
    parsed_coord_pairs = []
    for line in coord_pairs:
        line_pairs = []
        for coord in line:
            line_pairs.append(
                Coord(x=int(coord.split(",")[0]), y=int(coord.split(",")[1]))
            )
        parsed_coord_pairs.append(line_pairs)

    max_x = 0
    max_y = 0
    for coord_pair in parsed_coord_pairs:
        for coord in coord_pair:
            if coord.x > max_x:
                max_x = coord.x
            if coord.y > max_y:
                max_y = coord.y

    base_grid = [[0] * (max_x + 1) for _ in range(max_y + 1)]

    for coord_pair in parsed_coord_pairs:
        if coord_pair[0].x == coord_pair[1].x:
            min_y = min(coord_pair[0].y, coord_pair[1].y)
            max_y = max(coord_pair[0].y, coord_pair[1].y)
            for i in range(min_y, max_y + 1):
                base_grid[i][coord_pair[0].x] += 1
        elif coord_pair[0].y == coord_pair[1].y:
            min_x = min(coord_pair[0].x, coord_pair[1].x)
            max_x = max(coord_pair[0].x, coord_pair[1].x)
            for i in range(min_x, max_x + 1):
                base_grid[coord_pair[0].y][i] += 1

    print(len([y for x in base_grid for y in x if y >= 2]))


if __name__ == "__main__":
    main()
