from sys import argv


def fact(n: int) -> int:
    """
    Find the factorial if a number
    :return: int
    """

    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


def main():
    print(fact(int(argv[1])))
