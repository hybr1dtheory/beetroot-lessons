# Task 1
def slice_str(s):
    return '' if len(s) < 2 else s[:2] + s[-2:]


# Task 2
def check_phone(phone):
    return phone.isdigit() and len(phone) == 10


# Task 3
def math_quiz():
    attempts = 3
    print('Enter what the expression 16 - 8 / 2 * 4 is equal to.')
    while attempts > 0:
        answer = input(f'You have {attempts} attempts.\n')
        if int(answer) == 0:
            print('Absolutely right!\n')
            break
        else:
            print('Wrong answer. Try again.\n')
    attempts -= 1


# Task 4
def check_name(name):
    my_name = 'illia'
    return my_name == name.lower()


print(slice_str(input('TASK 1: \nEnter some string to slice:\n')), '\n')
print(check_phone(input('TASK 2: \nEnter phone number to check:\n')), '\n')
print('TASK 3:')
math_quiz()
print(check_name(input('TASK 4: \nEnter name to check:\n')))