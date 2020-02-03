import random

r = random.randint(1, 100)
while True:
	 num = input('please guess a number: ')
	 num = int(num)
	 if num == r:
	 	print('correct')
	 	break
	 elif num > r:
	 	print('it\'s bigger than answer')
	 elif num < r:
	 	print('it\'s smaller than answer')

