n = int(input("n=")) 
k = 1 
suma = 0 
wynik = 0 
while suma + k <= n: 
    suma += k 
    k += 2 
    wynik += 1 
print(wynik)