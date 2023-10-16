""" type_hints """
from typing import Sequence


def headline(text: str, is_align: bool = False) -> str:
    """ headline """
    return text.title() if is_align else text.title().center(len(text) * 2, "x")


def get_first_element(data: Sequence[int]) -> int:
    """ get_first_element """
    return data[0]


# reveal_type ( headline -)
# reveal_locals()


if __name__ == "__main__":
    print(headline("hello world", is_align=True))
    print(headline.__annotations__)
    print(headline.__dict__)
    print(get_first_element([1, 2, 3]))
