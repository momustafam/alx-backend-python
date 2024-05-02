#!/usr/bin/env python3
'''Simple module since it has only a one simple function sum_list(input_list).'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Calculate the summation of given sequence of float numbers.

        Parameters:
            - input_list (list[float,...]): the list of float numbers

        Return: the sum of `input_list` as float
    '''
    return sum(input_list)
