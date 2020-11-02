import random 
answer = random.randint(1,6)
while True:
	try:
		guess = int(input('Guess a number 1~6:  '))
		if 0 < guess < 7:
			if answer == guess:
				print('you guessed right!')
				break
			else:
				print('guess again')
		else:
			print('the number must be between 1 and 6')
	except:
		print('type a number')
