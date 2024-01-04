import argparse
from functools import wraps
from typing import Callable, Any


def parse_args(func: Callable[[int], bool]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper() -> bool:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "value", type=int, help="The integer to check for primality."
        )
        args = parser.parse_args()
        return func(args.value)

    return wrapper
