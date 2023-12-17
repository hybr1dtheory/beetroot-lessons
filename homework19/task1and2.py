def with_index(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1


def in_range(start: int, end: int, step=1):
    if not isinstance(step, int) or step == 0:
        raise ValueError("step parameter must be an integer not equals to 0")
    elif step < 0 and start < end:
        raise ValueError("start must be greater than end when step is negative")
    elif step > 0 and start > end:
        raise ValueError("start must be lower than end when step is positive")
    if start <= end:
        val = start
        while val < end:
            yield val
            val += step
    else:
        val = start
        while val > end:
            yield val
            val += step


if __name__ == "__main__":
    s = "abcdefg"
    for i, c in with_index(s, 1):
        print(i, '-', c)

    print(*in_range(1, 10))
    print(*in_range(0, -10, -1))
