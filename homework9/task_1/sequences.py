"""This module contains function for calculate nth element of the Lukas sequence.
By default, it calculates nth element of the Lukas numbers, but some special cases
of this sequence (Fibonacci numbers: l0 = 0, l1 = 1)  can be calculated too."""


def lukas(n, l0=2, l1=1):
    if n == 0:
        return l0
    if n == 1:
        return l1
    for _ in range(n-1):
        l0, l1 = l1, l0 + l1
    return l1


if __name__ == '__main__':
    num = int(input('Enter the number of element:\n'))
    print(lukas(num))
