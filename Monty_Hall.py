import random

def montyHallExperiment(s, chosen, change):
	doors = []
	for door in range(s):
		doors.append('EMPTY')
	doors[random.randint(0,s-1)] = 'GOAT' #put the goat behind a random door
	if chosen == 0:
		chosen = random.randint(0,s)

	#DELETE ALL DOORS EXCEPT CHOSEN DOOR AND DOOR WITH THE GOAT
	#0 will be the chosen door and 1 will be one of the other doors
	if doors[chosen-1] == 'GOAT':
		doors = ['GOAT','EMPTY']
	else:
		doors = ['EMPTY','GOAT']
	if change: return doors[1] #User changed the selection
	else: return doors[0] #User didn't change the selection

def checkGreaterThan0 ():
	n = -1
	while n < 1:
		try:
			n = int(input(''))
			if n < 1:
				print('Type a number greater than 0')
		except ValueError:
			print('Type a number greater than 0')
	return n

def checkYesNo():
	b = -1
	while b != True and b != False:
		b = input('').lower()
		if b == 'y': b = True
		elif b == 'n': b = False
		else: print('Type "y" for yes or "n" for no')
	return b

print('This is a Monty-Hall simulator! If you don\'t know what is Monty-Hall problem, you can read more about here https://en.wikipedia.org/wiki/Monty_Hall_problem.')
print('Steps:\n1.Typically, Monty-Hall problem is arised with 3 doors, but you can obtain clearer results by increasing doors amount.\n2.Choose the door where you think the goat is, but as you can guess, that\'s irrelevant at this point.\n3.All other doors are deleted, except one door. Now you have 2 doors and goat is behind one of them.\n4.You must choose keep your door or pick the other one (╭Õ_ õ )\n5.You can repeat the experiment with this choices as many times as you want. This way, you could obtain results faster than one by one.\nIMPORTANT! You can repeat the experiment with the same doors amount, so you could change some decisions and see how success percentage change. You can restart the whole experiment and change doors amount as well, and results will restart too.')

while True:
	total_goats = 0 #Number of found goats in total for the same doors amount
	total_tries = 0 #Number of tries for different choices but with the same doors amount
	size = -1 #Amount of doors
	repeat_size = -1 #Repeat the experiment with same size

	print('\nHow many doors do you want?\nIt is recomended a maximum of 1000 doors for fast performance')
	size = checkGreaterThan0()
	while repeat_size:
		goats = 0 #Number of found goats
		tries = -1 #Number of tries for specific choices
		chosen_door = -1 #Door selected by the user
		change_door = -1 #If user want to change the door
		decision = '' #It says in words if door was change

		if total_tries > 0: print('')
		print(f'What door do you want to pick? (between 1 and {size}, type 0 for random doors in each repetition)')
		while chosen_door < 0 or chosen_door > size:
			try:
				chosen_door = int(input(''))
				if chosen_door < 0 or chosen_door > size:
					print(f'Type a number between 0 and {size}')
			except ValueError:
				print(f'Type a number between 0 and {size}')
		print('Do you want to change your door? (y/n)')
		change_door = checkYesNo()
		if change_door: decision = 'changed'
		else: decision = 'didn\'t change'
		print('How many times do you want to repeat the experiment for this choices?\nIt is recomended a maximum of 100000 repetitions for fast performance')
		tries = checkGreaterThan0()

		for i in range(tries):
			if montyHallExperiment(size, chosen_door, change_door) == 'GOAT':
				goats += 1
		total_goats += goats
		total_tries += tries

		print(f'\nYou {decision} your door when you were asked for and this is the result:')
		print(f'Found goats = {goats}')
		print(f'Tries = {tries}')
		print(f'Success = {goats*100/tries}%')
		if (total_tries > tries):
			print(f'\nTotal found goats = {total_goats}')
			print(f'Total tries = {total_tries}')
			print(f'Total success = {total_goats*100/total_tries}%')
		print(f'Your experiment has {size} doors')

		print('\nDo you want to repeat experiment for the same doors amount? (y/n)\nRemember, if you keep the door amount goats will be add to existing and you could change the other decisions')
		repeat_size = checkYesNo()