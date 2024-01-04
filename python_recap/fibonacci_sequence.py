from typing import Dict, Any


def fibonacci_sequence(dept: int) -> Dict[str, Any]:
    """
    Generate a Fibonacci sequence up to the specified depth.

    Parameters:
    - depth (int): The number of Fibonacci numbers to generate. Must be a positive integer.

    Returns:
    - dict: A dictionary containing:
        - 'result': A list of Fibonacci numbers up to the specified depth.
        - 'sum': The sum of all the Fibonacci numbers in the result list.

    Example:
    >>> fibonacci_sequence(5)
    {'result': [0, 1, 1, 2, 3], 'sum': 7}
    """
    _prev, _current = 0, 1
    counter = 2
    list_result = [_prev, _current]

    while counter <= dept:
        _next = _prev + _current
        list_result.append(_next)
        _prev, _current = _current, _next
        counter += 1

    return {"result": list_result, "sum": sum(list_result)}


if __name__ == "__main__":
    print(fibonacci_sequence(10))
