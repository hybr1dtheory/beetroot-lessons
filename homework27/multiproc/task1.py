from multiprocessing import Pool
from os import cpu_count
from time import perf_counter


def is_prime(num: int) -> int | bool:
    """this function implements a simple algorithm for primality test
    with a complexity O(sqrt(n))"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return num


def filter_primes(numbers: list[int], np=None):
    """this function divides the calculation into
    a specified number of processes using a process pool.
    All available processor cores are used by default"""
    if np is None:
        num_proc = cpu_count()
    else:
        num_proc = np
    print(num_proc)
    with Pool(processes=num_proc) as pool:
        prime_numbers = pool.map(is_prime, numbers)
    return [num for num in prime_numbers if num]


NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]


start = perf_counter()
result = filter_primes(NUMBERS, 4)
print(result)
finish = perf_counter() - start
print(finish)
