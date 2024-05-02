#!/usr/bin/env python3
'''Simple module since it has a simple function make_multiplier(multiplier).'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        creates a multiplier function

        Args:
            multiplier (float): multiplier to multiply with

        Returns:
            a function that multiplies a float by multiplier
    """
    def f(x: float) -> float:
        """
            multiplies x by multiplier

            Args:
                x (float): number

            Returns:
                x * multiplier
        """
        return x * multiplier
    return f
