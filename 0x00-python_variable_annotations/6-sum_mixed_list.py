#!/usr/bin/env python3
from typing import List, Union
"""
Task 6 Complex types - mixed list

a type-annotated function sum_mixed_list
 which takes a list mxd_lst
 of integers and floats and returns their sum as a float.

"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list function

    Args:
      mxd_list (List[Union[int, float]): list with mixed values to be summed.

    Returns:
      float: Returns a summed value which is a float

    """
    ans: float = 0.0

    for item in range(0, len(mxd_lst)):
        ans = ans + mxd_lst[item]

    return ans
