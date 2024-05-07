#!/usr/bin/env python3
'''Simple module since it has a simple function.'''
from typing import Generator
from random import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    '''coroutine yield a random number between 0 and 10.'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random()*10
