import utils

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

def task(n):
	_sum = 0
	for i in range(2, n):
		if utils.is_prime(i):
			_sum += i
	return _sum

def program():
	print("Answer: ", task(2000000))