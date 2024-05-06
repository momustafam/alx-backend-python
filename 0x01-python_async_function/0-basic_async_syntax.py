#!/usr/bin/python3
'''Simple module since it has an asynchronous func wait_random(max_delay).'''
import random
import asyncio


async def wait_random(max_delay=10):
    '''Coroutine that waits for a random delay between 0 and `max_delay`.'''
    val = random.random() * max_delay
    await asyncio.sleep(val)
    return val
