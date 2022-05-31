
# Which starting number, under one million, produces the longest chain?

def colatz_num(n):
	if n % 2 == 0:
		return n/2
	return 3*n+1

def colatz_count(n):
	count = 1
	while n != 1:
		n = colatz_num(n)
		count += 1
	return count

def task(n):
	biggest_count = 0
	number = 0
	for i in range(1, n):
		print(i)
		count = colatz_count(i)
		if count > biggest_count:
			number = i
			biggest_count = count
	return number


def program():
	print("Answer: ", task(1000000))