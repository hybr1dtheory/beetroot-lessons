import random as rd


# Task 1
def guess_number():
    num = rd.randint(1, 10)
    print('Welcome to the game "Guess the number"!')
    attempts = 3
    while attempts > 0:
        answer = int(input(f'Enter the integer from 1 to 10. You have {attempts} attempts:\n'))
        if answer == num:
            print('Great! Right answer, you win!')
            break
        else:
            attempts -= 1
            print('Wrong answer.')
    else:
        print('Sorry, you lose. Maybe next time.')


# Task 2
def birthday():
    name = input('Enter your name:\n')
    age = int(input('Enter your age:\n'))
    print(f'Hello {name}, on your next birthday you’ll be {age+1} years')


# Task 3
def shake_string():
    word = input('Enter some string:\n')
    for _ in range(5):
        chars = list(word)
        rd.shuffle(chars)
        word = ''.join(chars)
        print(word)


choice = input('Choose what function you want to run (enter an integer): \n1 - guess number \n2 - birthday \n3 - shake string\n')
if choice == '1':
    guess_number()
elif choice == '2':
    birthday()
elif choice == '3':
    shake_string()
else:
    print('Wrong input')