n = int(input("n="))
i = 1 
while i * i < n:
    if n%i == 0:
        print(i)
        print(int(n/i))
    i += 1
if i * i == n:
    print(i)