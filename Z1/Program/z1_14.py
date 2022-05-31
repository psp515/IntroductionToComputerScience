def silnia(n):
    wynik = 1 
    for i in range (1, n+1):
        wynik = wynik * i 
    return wynik

x = float(input("x="))
wynik = 1.0
n = 2 
while n <= 10:
    if n%4 == 0:
        wynik += (x**n)/(silnia(n))
    else:
        wynik -= (x**n)/(silnia(n))
    n += 2
print(wynik)