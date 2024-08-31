"""This module simulates the '100 prisoners problem' and calculates the probability of success
with the optimal strategy. By default, the parameters from the classic version of the problem
are used, but it allows calculation with any values of the parameters 'number of boxes',
'number of prisoners', 'number of attempts'.
About the problem: https://en.wikipedia.org/wiki/100_prisoners_problem"""
from random import shuffle


def try_once(n_boxes: int, n_pris: int, attempts: int) -> int:
    """This function simulates one attempt for n_pris prisoners.
    If at least one prisoner does not find his number, the function returns 0
    (according to the problem, this means a loss for everyone).
    If everyone has found their number, it returns 1.
    n_boxes - number of boxes in the room (n_boxes >= n_pris),
    n_pris - number of prisoners (n_pris > 0),
    attempts - number of boxes allowed to be opened in search of a number (0 < attempts < n_boxes)"""
    if n_boxes < n_pris:
        raise ValueError("n_boxes must be greater than or equal to n_pris")
    if n_pris < 1:
        raise ValueError("n_pris must be greater than 0")
    if not (0 < attempts < n_boxes):
        raise ValueError("attempts must be in range: 0 < attempts < n_boxes")
    boxes = [i for i in range(n_boxes)]
    numbers = [i for i in range(n_boxes)]
    shuffle(numbers)  # simulate the shuffling of numbers in boxes
    pack = dict(zip(boxes, numbers))
    for prisoner in range(n_pris):
        num = pack[prisoner]
        for _ in range(attempts):
            if num == prisoner:
                break
            num = pack[num]
        else:  # executes if break was not triggered in any iteration (number not found)
            return 0
    return 1


def simulate(cnt: int, boxes=100, prisoners=100, attempts=50) -> float:
    """This function runs the simulation cnt times and calculates the probability of success
    with the given parameters.
    cnt - number of simulation rounds (cnt > 0),
    boxes - number of boxes in the room (boxes >= prisoners),
    prisoners - number of prisoners (prisoners > 0),
    attempts - number of boxes allowed to be opened in search of a number (0 < attempts < boxes)"""
    if not isinstance(cnt, int):
        raise TypeError("The cnt argument must be an integer")
    if cnt < 1:
        raise ValueError(f"cnt must be greater than 0, but {cnt} was given")
    success = 0
    for _ in range(cnt):
        success += try_once(boxes, prisoners, attempts)
    return round(success/cnt, 2)


if __name__ == "__main__":
    print(simulate(100000) * 100, '%', sep='')
