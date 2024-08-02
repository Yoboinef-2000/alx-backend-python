#!/usr/bin/env python3

"""Type annotated sum_mixed_list function."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum'em up."""
    sum = 0
    for anElement in mxd_lst:
        sum += anElement
    return (sum)
