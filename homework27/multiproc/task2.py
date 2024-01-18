"""In this task we implement multiprocessing counter of prime numbers in a range
(with a shared list for all processes) and compare results with simple realisation."""
from multiprocessing import Process, Lock, Manager
from time import perf_counter
from random import randint


def miller_rabin_test(n: int, k=20) -> bool:
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
        a = randint(2, n - 1)
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


def find_primes(res_list, lck: Lock, proc_id: int):
    """Finding all prime numbers in range from 10 millions
    to 10 millions plus 1000000 * num_proc (1000000 numbers per process)."""
    beg = 10000000
    step = 1000000
    n = proc_id * step + beg
    res = [i for i in range(n, n + step) if miller_rabin_test(i)]
    lck.acquire()  # Attempt to get block
    try:
        res_list.extend(res)  # Change shared resource
    finally:
        lock.release()  # Releasing a lock after changing


if __name__ == "__main__":
    start = perf_counter()
    with Manager() as manager:
        # Creating shared list to write results
        shared_resource = manager.list()
        lock = Lock()
        num_processes = 8  # Number of processes
        processes = [Process(target=find_primes, args=(shared_resource, lock, i)) for i in range(num_processes)]
        for process in processes:
            process.start()
        for process in processes:
            process.join()
        print("Total amount of prime numbers: ", len(shared_resource))
    finish = perf_counter() - start
    print(f"Multiprocessing function finish with time: {finish}")

    start = perf_counter()
    res = [i for i in range(10000000, 18000000) if miller_rabin_test(i)]
    print("Total amount of prime numbers: ", len(res))
    finish = perf_counter() - start
    print(f"Simple synchronous code finish with time: {finish}")
