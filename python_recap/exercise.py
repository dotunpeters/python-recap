from sys import argv
from typing import List
import time


def main() -> List[int]:
    x = [1, 2, 4, 6, 9, 10, 14, 15, 17]
    return [
        4 * i if val % 2 == 0 else 9 * i if val % 3 == 0 else val * 2
        for i, val in enumerate(x)
    ]


def multiple_list() -> List[List[int]]:
    n: int = int(argv[1])
    output = []
    for i in range(1, n + 1):
        curr_list = []
        for j in range(1, 6):
            curr_list.append(i * j)
        output.append(curr_list)
    return output


def create_lists_linear():
    start_time = time.time()
    n: int = int(argv[1])
    _ = [
        [index, 2 * index, 3 * index, 4 * index, 5 * index] for index in range(1, n + 1)
    ]
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time
