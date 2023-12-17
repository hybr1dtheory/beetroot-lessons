from task3 import TypeDecorators
from task1 import User


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
