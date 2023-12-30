"""
    This is the package main entry point
"""


def main(message: str) -> None:
    """Summary

    :param message: The message to be displayed
    :type message: str
    raises: :class:`RuntimeError`: Out of fuel

    :return: Returns no value
    :rtype: None
    """
    print(f"message: {message}", len(message))


if __name__ == "__main__":
    main("Greetings from main package")
