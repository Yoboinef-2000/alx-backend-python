#!/usr/bin/env python3

"""Type annotateed element_length function."""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Get that length, and possibly girth."""
    return [(i, len(i)) for i in lst]
