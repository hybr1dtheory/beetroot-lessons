"""In this task a delay is added to each function to simulate the waiting
for a response to a request (or something similar)"""
import asyncio
from time import perf_counter


async def factorial(num: int):  # alone running - 20.0475s
    f = 1
    for i in range(1, num + 1):
        print("computing factorial...")
        f *= i
        await asyncio.sleep(2)
    print(f"Result of factorial function: {f}")


async def generate_ascii(start: int):  # alone running - 15.0943s
    my_list = []
    for i in range(start, start + 15):
        print("Generating list...")
        await asyncio.sleep(1)
        my_list.append(chr(i))
    print(*my_list)


async def just_wait():  # alone running - 16.209s
    for i in range(20):
        print("Waiting...")
        await asyncio.sleep(0.8)
    print("End of waiting")


# Tasks are added to the event loop and start executing in the order they are added
# using the asyncio.gather() function. During the delay, the event loop switches
# to another task, so the total execution time is almost exactly equal to the execution time
# of the longest task (factorial - about 20 seconds). When all three functions
# are executed synchronously, we get a total time of approximately 51 seconds.
async def main():
    beg = perf_counter()
    tasks = [factorial(10), generate_ascii(65), just_wait()]
    await asyncio.gather(*tasks)
    end = perf_counter() - beg
    print(end)


if __name__ == "__main__":
    asyncio.run(main())
