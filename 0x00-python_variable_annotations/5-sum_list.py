#!/usr/bin/env python3

"""Type annotated sum_list function."""
from typing import List

def sum_list(input_list: List) -> float:
    """Sum'em up."""
    sum = 0
    for elementInTheList in input_list:
        sum += elementInTheList
    return sum
