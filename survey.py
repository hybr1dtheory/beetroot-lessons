n = int(input('Enter number of respondents:\n'))
answers = []
for i in range(n):
	print(f'Questions for respondent #{i+1}')
	name = input('Enter your name:\n')
	age = int(input('Enter your age:\n'))
	brand = input('What brand of smartphone are you currently using?\n')
	answers.append((name, age, brand))

ages = [i[1] for i in answers]
print('\nAverage age of respondents:', int(sum(ages) / len(ages)))
brands = set([i[2] for i in answers])
print('Unique brand names:', *brands, sep='\n')
