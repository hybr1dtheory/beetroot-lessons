import threading
import time


def factorial(num: int):
    f = 1
    for i in range(1, num + 1):
        print("computing factorial...")
        f *= i
        time.sleep(2)
    print(f"Result of factorial function: {f}")


def generate_ascii(start: int):
    my_list = []
    for i in range(start, start + 15):
        print("Generating list...")
        time.sleep(1)
        my_list.append(chr(i))
    print(*my_list)


def just_wait():
    for i in range(20):
        print("Waiting...")
        time.sleep(0.8)
    print("End of waiting")


def main():
    functions = [(factorial, [10]), (generate_ascii, [65]), (just_wait, [])]
    threads = []
    for item in functions:
        func, arg = item
        trd = threading.Thread(target=func, args=arg)
        threads.append(trd)
        trd.start()
    for trd in threads:
        trd.join()


if __name__ == "__main__":
    beg = time.perf_counter()
    main()
    end = time.perf_counter() - beg
    print(end)
