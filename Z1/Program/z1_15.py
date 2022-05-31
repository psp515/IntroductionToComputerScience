def sqrt(s):
    n = 1.0
    while abs(n*n-s) > 0.0000001:
        n = (s/n + n)/2
    return n 

wynik = sqrt(0.5)
iloczyn = 1
n = 1 
while n <= 100:
    iloczyn = iloczyn * wynik
    wynik = sqrt(0.5 + 0.5 * wynik) 
    n += 1
print(2.0 / iloczyn)