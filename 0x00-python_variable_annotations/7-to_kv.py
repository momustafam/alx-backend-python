#!/usr/bin/env python3
'''Simple module since it has only a one simple function to_kv(k, v).'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        returns a tuple

        Args:
            k (str): key
            v (int | float): value

        Returns:
            tuple (k, v^2)
    """
    return (k, v ** 2)
