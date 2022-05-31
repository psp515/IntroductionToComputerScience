import math

import utils

#What is the value of the first triangle number to have
# over five hundred divisors?

def divisors_count(n):
	counter = 0
	for i in range(1, int(math.sqrt(n)) + 1):
		if n % i == 0:
			counter += 2
	return counter - 1 if n % math.sqrt(n) == 0 else counter

def task(n):
	triangle = 1
	i = 2
	while True:
		if divisors_count(triangle) > n:
			return triangle
		triangle += i
		i += 1
	return triangle

def program():
	print("Answer: ", task(500))