def silnia(n):
    if n == 0: 
        return 1
    result = 1 
    for i in range (1, n+1):
        result = result * i 
    return result 

e = 0 
for i in range (0,20):
    e += 1/silnia(i) 

print(e)