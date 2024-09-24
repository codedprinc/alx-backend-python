#!/usr/bin/env python3
from typing import Union, Tuple
"""
task 7 Complex types - string and int/float to tuple

a type-annotated function to_kv that
 takes a string k and an int OR float v
as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v
and should be annotated as a float.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv function

    Args:
      k (str): First parameter

      v (Union[int, float]): second parameter

    Returns:
      Tuple: Returns a tuple whose first element is `k` and
        second element is the square of the int/float v and
        should be annotated as a float.

    """
    v_2: float = v ** 2

    return (k, v_2)
