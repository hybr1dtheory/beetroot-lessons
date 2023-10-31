from random import randint


# Task 1
print('\tTask 1')
rand_lst = [randint(1, 100) for i in range(10)]
print(f'The max element of the list {rand_lst} is: {max(rand_lst)}', end='\n\n')

# Task 2
print('\tTask 2')
lst_1 = [randint(1, 10) for _ in range(10)]
lst_2 = [randint(1, 10) for _ in range(10)]
res_lst = list(set(lst_1 + lst_2))
print(*res_lst, end='\n\n')

# Task 3
print('\tTask 3')
res_nums = [i for i in range(1, 101) if (i % 7 == 0 and i % 5 != 0)]
print(*res_nums)
