import math
import utils

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def summer(a, b):
	return a + b + math.sqrt(a * a + b * b)

def task(n):
	for i in range(1, n):
		for j in range(1, n):
			if j > i:
				break
			a = i * j
			b = (i*i-j*j)/2
			c = (j * j + i * i) / 2
			if a+b+c == 1000:
				return a*b*c

def program():
	print("Answer: ", task(1000))