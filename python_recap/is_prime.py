"""is_prime python module"""
from python_recap.utils import parse_args


@parse_args
def is_prime(value: int) -> None:
    """Returns True if value is prime and False otherwise.

    :param value:
    :type value: int

    :return:
    :rtype: None
    """
    if value == 1:
        print("False")
        return
    for i in range(2, value):
        div_remainder = value % i
        if div_remainder == 0:
            print("False")
            return
    print("True")
