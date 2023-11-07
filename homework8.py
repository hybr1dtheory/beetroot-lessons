# Task 1
def favorite_movie(name):
	print(f'My favorite movie is named {name}')


# Task 2
def make_country(country, capital):
	d = {country: capital}
	print(d)


# Task 3
def add_all(*args):
	return sum(args)


def subtract(*args):
	result = args[0]
	for i in args[1:]:
		result -= i
	return result


def mult_all(*args):
	result = args[0]
	for i in args[1:]:
		result *= i
	return result


def make_operation(oper, *args):
	opers = {'+': add_all, '-': subtract, '*': mult_all}
	func = opers[oper]
	return func(*args)


# Examples
favorite_movie('Alex')
make_country('Ukraine', 'Kyiv')
print(make_operation('*', 2, 3, 5, 8, 13))
