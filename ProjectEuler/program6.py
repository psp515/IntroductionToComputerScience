import utils


# Find the difference between the sum of the
# squares of the first one hundred natural numbers and
# the square of the sum

def task(n):
	return ((n+1)*n/2)**2-n*(n+1)*(2*n+1)/6

def program():
	print("Answer: ", task(100))