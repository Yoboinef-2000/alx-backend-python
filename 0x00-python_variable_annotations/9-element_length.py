#!/usr/bin/env python3

"""Type annotateed element_length function."""
from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Get that length, and possibly girth."""
    return [(i, len(i)) for i in lst]
