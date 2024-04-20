import asyncio
import time
import math

async def hw():
    y = math.factorial(1000000)
    await asyncio.sleep(0)
async def hw_sleep():
    z = math.factorial(1000000)
    await asyncio.sleep(0)
async def main():
    t1 = time.time()
    await asyncio.gather(hw(), hw_sleep())
    t2 = time.time()
    print(t2 - t1)
asyncio.run(main())
