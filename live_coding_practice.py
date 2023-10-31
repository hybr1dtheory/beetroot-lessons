# Task 1
name = input('Enter your name:\n')
surname = input('Enter your surname:\n')
dom = input('Enter the domain of the mail service (for example: gmail.com):\n')

var1 = f'{name}.{surname}@{dom}'
var2 = f'{name}-{surname}@{dom}'
var3 = f'{name[0]}.{surname}@{dom}'

print('Suggested Email Address Options:', var1, var2, var3, sep='\n')


# Task 2
age = int(input('Enter your age:\n'))
if age >= 18:
    print('Alcohol is allowed')
elif age >= 14:
    print('Energetic drinks are allowed')
else:
    print("Все окрім алкоголю і енергетиків")

# Task 3
line = input()
correct_line = line[1:-1]
print(correct_line)

# Task 4
line = input()
print(line.replace("&", ''))

# Task 2/1
age = 40
income = 20000
has_job = True
max_age, min_inc = 70, 18000
if income >= min_inc and age <= max_age and has_job:
    print('Give credit')
else:
    print('No')

# Task 2/2
age = 20
email = 'example@gmail.com'
passw = '123456789d'
has_digit, has_alpha = False, False
age_check = 18 <= age
len_check = len(passw) >= 8
for s in passw:
    if s.isdigit():
        has_digit = True
    if s.isalpha():
        has_alpha = True
if has_digit and has_alpha and len_check and age_check and email:
    print('Confirm user')
else:
    print('Access denied')
