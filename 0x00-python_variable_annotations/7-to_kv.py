#!/usr/bin/env python3

"""Type annotated to_kv function."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Square'em up."""
    return (k, float(v ** 2))
