# Task 1
def func(a=5, b=10):
    c = a + b
    return locals()


# Task 2
def create_qfunc(a, b, c):
    """Create a quadratic function with coefficients a, b, c
    that calculates the value of a function (y) at a given point (x)"""
    def quad_func(x):
        return a * x**2 + b * x + c
    return quad_func


# Task 3
def choose_func(nums: list, f1, f2):
    if all([i >= 0 for i in nums]):
        return f1(nums)
    else:
        return f2(nums)


def square_nums(nums: list):
    return [i**2 for i in nums]


def remove_negatives(nums: list):
    return [i for i in nums if i >= 0]


# Testing
print('Number of Local variables: ', len(func()))
qfunc = create_qfunc(1, 2, 5)
print("Result of function x^2 + 2x + 5 when x = 5: ", qfunc(5))
nums1 = [i for i in range(1, 10)]
nums2 = [i for i in range(-5, 6)]
print('Result of task 3 if all numbers are positive: ', choose_func(nums1, square_nums, remove_negatives))
print('Result of task 3 if there are negative nums: ', choose_func(nums2, square_nums, remove_negatives))
