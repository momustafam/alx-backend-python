#!/usr/bin/env python3
'''Simple module since it has a simple function sum_mixed_list(mxd_list).'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''Calculate the summation of a list of integers and floats.

        Parameters:
            - mxd_list (List[Union[int, float]]): a list of integers and floats

        Return: the summartion of `mxd_list`
    '''
    return sum(mxd_list)
