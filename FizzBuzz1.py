upperLimit = 100
numberTextUnits = ["one", "two","three","four","five","six","seven","eight", "nine"]
numberTextTens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
numberText = []


print "Fizz buzz counting up to %s" % upperLimit
for number in range(1, upperLimit+1):
	if (number % 3 == 0 ) and (number % 5 == 0):
		print "fizz buzz "
	elif (number % 3 == 0):
		print "fizz"
	elif (number % 5 == 0):
		print "buzz"
	else:
		print str(number)

