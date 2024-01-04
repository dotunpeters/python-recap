from sys import argv
import time


def fibo(val: int) -> int:
    """
    return the nth term of a fibonacci sequence using recursion
    :param val:
    :return: int
    """

    # base cases
    if val == 1:
        return 0

    if val == 2 or val == 3:
        return 1

    return fibo(val - 1) + fibo(val - 2)


def main() -> None:
    start_time = time.time()
    print(fibo(int(argv[1])))
    end_time = time.time()
    print("Time: ", end_time - start_time)


if __name__ == "__main__":
    main()
