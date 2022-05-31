i = 1
while i < 1000000:
    j = 1
    suma = 0
    while j * j < i: 
        if i%j == 0:
            suma = suma + j + i/j 
        j += 1
    if j * j == i:
        suma += j 
    suma -= i 
    k = 1
    suma2 = 0
    while k * k < suma:
        if suma%k == 0:
            suma2 = suma2 + k + suma/k
        k+= 1
    if k * k == suma:
        suma2 += k 
    suma2 -= suma 
    if int(i) == int(suma2) and int(i) < int(suma) and int(i) != int(suma):
        print(str(i) + " " + str(int(suma)))
    i += 1