from task3 import TypeDecorators
from task1 import User
from task2 import Worker, Boss


# Task 3 testing
@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_str
def add(a: int | float, b: int | float):
    return a + b


@TypeDecorators.to_float
def get_str_float(left: str, right: str):
    return left + '.' + right


assert do_nothing('25') == 25
assert do_something('True') is True
assert add(5, 7) == '12'
assert get_str_float('2', '055') == 2.055


# Task 1 testing
# Valid emails
assert User.validate('user@example.com')
assert User.validate('name_with_underscores@x.org')
assert User.validate('long.email-address-with-hyphens@and.subdomains.example.com')
assert User.validate('x@exam-ple.com')
assert User.validate('very.common22@example1.com')
# Invalid emails
print(User.validate('abc.example.com'))
print(User.validate('a@b@c@example.com'))
print(User.validate('i.like.underscores@but_they_are_not_allowed_in_this_part.com'))
print(User.validate('abc@example.222'))


# Task 2 testing
b1 = Boss(1, "First Boss", "Beetroot")
w1 = Worker(1, "John Smith", "Beetroot", b1)
w2 = Worker(2, "Sam Adams", "Beetroot", b1)
w3 = Worker(3, "James Black", "Beetroot", b1)
b1.add_worker(w1, w2, w3)
print(*b1.get_workers(), sep='\n')
b2 = Boss(2, "Second Boss", "Another company")
print(w3.boss.name)
w3.boss = b2
print(w3.boss.name)
try:
    w3.boss = "another boss"
except ValueError:
    print("Only Boss type can be added to boss attribute")
try:
    b2.add_worker("some worker")
except ValueError:
    print("Only Worker type can be added to workers list")
