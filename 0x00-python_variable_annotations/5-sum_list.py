#!/usr/bin/env python3

"""Type annotated sum_list function."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum'em up."""
    total = 0.0
    for element in input_list:
        total += element
    return total
