import asyncio
from time import perf_counter


async def factorial(num: int):
    f = 1
    for i in range(1, num + 1):
        print("computing factorial...")
        f *= i
        await asyncio.sleep(2)
    print(f"Result of factorial function: {f}")


async def generate_ascii(start: int):
    my_list = []
    for i in range(start, start + 15):
        print("Generating list...")
        await asyncio.sleep(1)
        my_list.append(chr(i))
    print(*my_list)


async def just_wait():
    for i in range(20):
        print("Waiting...")
        await asyncio.sleep(0.8)
    print("End of waiting")


async def main():
    beg = perf_counter()
    tasks = [factorial(10), generate_ascii(65), just_wait()]
    await asyncio.gather(*tasks)
    end = perf_counter() - beg
    print(end)


if __name__ == "__main__":
    asyncio.run(main())
