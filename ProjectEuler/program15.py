import utils

#

def silnia(n):
	silnia = 1
	for i in range(1, n+1):
		silnia *= i
	return silnia

def task(n):
	return int((silnia(2*n))/(silnia(n)*silnia(n)))

def program():
	print("Answer: ", task(20))