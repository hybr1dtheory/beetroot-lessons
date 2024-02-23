# answers
# question6 - log n
# question3 - n^2
# question4 - n
# question5 - n^2
# question2 - 1
# ???? - n


# time complexity = O(n^2), because operation "if el_first_list in second_list" has
# complexity O(n) and is applied at each iteration.
def question1(first_list: list[int], second_list: list[int]) -> list[int]:
    res: list[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


# time complexity = O(1) because the number of iteration is a constant
def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


# time complexity = O(len(list1) * len(list2)) = O(n^2)
def question3(first_list: list[int], second_list: list[int]) -> list:
    temp: list = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


# time complexity - O(n) - iterating through the list
def question4(input_list: list[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


# complexity - O(n^2) because of nested loop with n iterations
def question5(n: int) -> list[tuple[int, int]]:
    res: list[tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


# complexity - O(log(n)) because each iteration the variable n is reduced by half
def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n
