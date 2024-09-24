#!/usr/bin/env python3
"""
Task 2 Basic annotations - floor

a type-annotated function floor which takes a float n as argument
and returns the floor of the float.
"""


def floor(n: float) -> int:
    """
    Floor function

    Args:
      n (float): Parameter for value to be floored.

    Returns:
      int: value to be returned after being floored

    Examples:
      >>> ans = floor(666.66)
      >>> print(ans)
      666

    """
    return int(n)
