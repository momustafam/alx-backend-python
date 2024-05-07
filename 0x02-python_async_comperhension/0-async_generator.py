#!/usr/bin/env python3
'''Simple module since it has a simple function.'''
from random import random
import asyncio


async def async_generator():
    '''coroutine yield a random number between 0 and 10.'''
    for i in range(10):
        yield random()*10
