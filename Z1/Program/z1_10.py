i = 1
while i < 1000000:
    j = 1
    suma = 0
    while j * j < i:
        if i%j == 0:
            suma += j 
            suma += i/j
        j += 1 
    if j*j == i:
        suma += j
    suma -= i
    if suma == i:
        print(i)
    i+= 1