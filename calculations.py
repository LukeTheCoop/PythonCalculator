import math

def calculation(num_one, num_two, operator):
	operators = ['+', '-', '*', '/', '**', 'sr']
	print (num_one, num_two, operator)
	if operator in operators:
		num_one, num_two, index = float(num_one), float(num_two), operators.index(operator)
		if index == 0:
			return num_one + num_two
		elif index == 1:
			return num_one - num_two
		elif index == 2:
			return num_one * num_two
		elif index == 3:
			return num_one / num_two
		elif index == 4:
			return num_one ** num_two
		elif index == 5:
			print(num_one)
			print(math.sqrt(num_one))
			return math.sqrt(num_one)

if __name__ == '__main__':
	pass