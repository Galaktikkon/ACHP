from copy import deepcopy

TREAT = "*"
WALL = "#"
CAT = "O"

DIRECTIONS = ["L", "P", "G", "D"]
MOVES = {"L": (0, -1), "P": (0, 1), "G": (-1, 0), "D": (1, 0)}


def read_input() -> tuple[int, int, int, list[list[str]]]:
    m, n, k = map(int, input().split())
    M = [list(input().strip()) for _ in range(n)]
    return m, n, k, M


def find_cat(M: list[list[str]], n: int, m: int) -> tuple[int, int]:
    for i in range(n):
        for j in range(m):
            if M[i][j] == CAT:
                return i, j
    raise Exception("No cat found!")


def slide_cat(
    M: list[list[str]], direction: str, i: int, j: int
) -> tuple[int, int, int]:
    x_translation, y_translation = MOVES[direction]
    eaten_treats = 0

    while True:
        next_i, next_j = i + x_translation, j + y_translation

        M[i][j] = WALL

        if M[next_i][next_j] == WALL:
            break

        i, j = next_i, next_j
        if M[i][j] == TREAT:
            eaten_treats += 1

    return i, j, eaten_treats


def backtracking(M: list[list[str]], k: int, i: int, j: int, S: list[str]) -> bool:
    if k <= 0:
        print("".join(S))
        return True

    for direction in DIRECTIONS:
        M_copy = deepcopy(M)

        new_x, new_y, eaten_treats = slide_cat(M_copy, direction, i, j)

        if (new_x, new_y) != (i, j):
            if backtracking(M_copy, k - eaten_treats, new_x, new_y, S + [direction]):
                return True

    return False


def main() -> int:
    m, n, k, M = read_input()
    i, j = find_cat(M, n, m)

    backtracking(M, k, i, j, [])

    return 0


if __name__ == "__main__":
    main()
