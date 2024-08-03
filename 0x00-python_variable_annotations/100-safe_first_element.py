#!/usr/bin/ env python3

"""Correcting duck-typed annotations."""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Duck'em up."""
    if lst:
        return lst[0]
    else:
        return None
