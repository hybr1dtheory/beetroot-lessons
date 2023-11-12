from random import randint


# Task 1
def oops():
	x = randint(0, 3)
	if x == 0:
		raise KeyError
	elif x == 1:
		raise IndexError
	elif x == 2:
		raise NameError
	else:
		print('No error was raised')


def test():
	try:
		oops()
	except (IndexError, KeyError):
		print('IndexError or KeyError was raised')
	except:
		print('Any another error was raised')
	finally:
		print('This block of code will execute regardless of whether an error was raised or not')


# Task 2
def sq_div():
	try:
		a = float(input('Enter 1st number:\n'))
		b = float(input('Enter 2nd number:\n'))
		return a**2 / b
	except ValueError:
		print('a and b must be numbers (integer or float)')
	except ZeroDivisionError:
		print('Division by zero is impossible')


# Run functions
test()
print(sq_div())
