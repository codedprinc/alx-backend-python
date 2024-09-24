#!/usr/bin/env python3
from typing import List
"""
Task 6. Complex types - mixed list

 a type-annotated function sum_list which takes
 a list input_list of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: List[float]) -> float:
    """
    sum_list

    Args:
      input_list (List[float]): Contains a list of floats (only).


    Returns:
      float: Returns the sum of the values as a float.
    """
    ans: float = 0.0
    for num in range(0, len(input_list)):
        ans = ans + input_list[num]

    return ans
