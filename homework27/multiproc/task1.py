from multiprocessing import Pool
from os import cpu_count
from time import perf_counter
import random


def miller_rabin_test(n: int, k=10) -> bool:
    """This function implements Miller–Rabin probabilistic primality test
    with complexity O(k*log3(n))"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def filter_primes(numbers: list[int], np=None) -> list[int]:
    """this function divides the calculation into
    a specified number of processes using a process pool.
    All available processor cores are used by default"""
    if np is None:
        num_proc = cpu_count()
    else:
        num_proc = np
    print(num_proc)
    with Pool(processes=num_proc) as pool:
        prime_numbers = pool.map(miller_rabin_test, numbers)
    return [num for num, is_pn in zip(NUMBERS, prime_numbers) if is_pn]


NUMBERS = [
    2, 1099726899285419, 1570341764013157, 1637027521802551,
    1880450821379411, 5477352563647856366372783, 1893530391196711,
    2447109360961063, 3, 2772290760589219, 3033700317376073,
    4350190374376723, 4350190491008389, 4350190491008390,
    2361183241434822606847, 4350222956688319, 11, 2305843009213693951,
    87178291199, 2305843009213694009, 479001599, 222333444555666789,
    2447120421950803, 147573952589676412927, 561, 567567432678986568,
    11111111111111111111111, 39916801, 9007199254740991,
    576460752303423487, 140737488355327, 1157587229, 10000079431,
    10000079447, 10000079477, 10000079501, 10000079513,
    10000079567, 10000079569, 10000079581, 10000079611,
    10000079623, 10000079627, 10000079629, 10000079659,
    10000079681, 10000079737, 10000079741, 10000079777
]


start = perf_counter()
result = filter_primes(NUMBERS, 4)
print(result)
finish = perf_counter() - start
print(finish)
