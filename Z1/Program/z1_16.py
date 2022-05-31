n = 2 
maxn = 0 
maxk = 0 
while n < 10000:
    i = n 
    kroki = 0 
    while i != 1: 
        i = (i%2)*(3*i+1) + (1-i%2)*i/2 
        kroki += 1 
    if kroki > maxk: 
        maxn = n 
        maxk = kroki 
    n += 1 
    print(n, " ", kroki)
print(maxn)