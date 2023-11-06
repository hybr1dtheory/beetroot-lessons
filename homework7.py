# Task 1
sen = input()
words = sen.split()
words_cnt = {}
for w in words:
    words_cnt[w] = words_cnt.get(w, 0) + 1
print(words)

# Task 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_cost = {}
for item in stock:
    total_cost[item] = stock[item] * prices[item]
print(total_cost)

# Task 3
lst = [(i, i*i) for i in range(1, 11)]
print(lst)

# Task 4
week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
num_week = {i+1: week[i] for i in range(7)}
week_num = {week[i]: i+1 for i in range(7)}
print(num_week)
print(week_num)
