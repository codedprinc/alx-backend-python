#!/usr/bin/env python3
from typing import Callable
"""
Task 8 Complex types - functions
a type-annotated function make_multiplier that takes a
 float multiplier as argument and
 returns a function that multiplies a float by multiplier.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier function

    Args:
      multiplier (float): The value to multiply

    Returns:
      Callable[[float], float]: A function that takes a float as input
        and returns the result of multiplying it by the `multiplier`.
    """

    def multiplier_func(x: float) -> float:
        """
        multiplier_func function

        Args:
          x (float): first parameter

        Returns:
          float : Value returned
        """
        return x * multiplier

    return multiplier_func
