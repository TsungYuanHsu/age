driving = input('Have you ever dirven a car?(yes/no) ')
if driving != 'yes' and driving != 'no':
	print('Please type yes or no')
	raise SystemExit

age = int(input('What is your age? '))
if driving == 'yes':
	if age >= 18:
		print('Pass!!')
	else:
		print('No, you are not allowed to drive at your age!!!')
elif driving == 'no':
	if age >= 18:
		print('You can get your car license.')
	else:
		year = 18 - age
		print('You can get your car license after', year, 'year(s).')