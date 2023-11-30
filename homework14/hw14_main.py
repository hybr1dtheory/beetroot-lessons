from decor import *


@logger
def add(x, y):
    return x + y


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


@ArgRules(type_=str, max_length=15, contains=['05', '@'])
def get_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# Task 1
print(add(7, 42))

# Task 2
print(create_slogan("Steve"))

# Task 3
print(get_slogan('johndoe05@gmail.com'))
print(get_slogan('05years'))
print(get_slogan('S@SH05'))
