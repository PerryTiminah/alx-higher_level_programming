#!/usr/bin/python3
def safe_print_integer(value):
    """print an interger with "{:d}".format().

    Args:
    value (int): The interger to print.

    Returns:
    If a TypeError or a ValueError - False.
    Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
