from .utils import parse_args
from typing import List


@parse_args
def is_perfect(value: int) -> None:
    """Returns True if the given number is a perfect number else False"""
    accumulator: int = 0
    for each in range(1, value // 2 + 1):
        if value % each == 0:
            accumulator += each
    if value == accumulator:
        return print(True)
    return print(False)
