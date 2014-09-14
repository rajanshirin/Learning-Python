import sys
def divisible (number1, number2):
	if number1 % number2 == 0:
		return True
	else:
		return False

def fizbuzz (upperLimit = 100):
	upperLimit = int (sys.argv[1])
	for number in range(1, upperLimit+1):
		if divisible(number, 3) and divisible (number, 5):
			print 'Fizzbuzz'
		elif (divisible(number, 3)):
			print 'Fizz'
		elif(divisible(number,5)):
			print 'Buzz'
		else:
			print str(number)

if __name__ == '__main__':
	fizbuzz()
	 