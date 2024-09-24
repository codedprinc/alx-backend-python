#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
"""
Task 9 Let's duck type an iterable object

Annotate the below functions parameters and return values with the appropriate types

"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length function

    Args:
      lst (Iterable[Sequence]): An iterable of sequences
        (e.g., lists, tuples, strings)

    Returns:
      List[Tuple[Sequence, int]]: A list of tuples,
        where each tuple contains a sequence from the input
        list and the length of that sequence.
    """
    return [(i, len(i)) for i in lst]
