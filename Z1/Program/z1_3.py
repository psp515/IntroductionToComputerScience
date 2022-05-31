zadana = int(input("suma=")) 
a = 1
b = 1
suma = 0 
while suma < zadana: 
    suma += a 
    c = a + b 
    a = b 
    b = c 
if suma == zadana: 
    print("Istnieje") 
else: 
    a = 1 
    b = 1 
    while suma > zadana: 
        suma -= a 
        c = a + b 
        a = b 
        b = c 
    if suma == zadana: 
        print("Istnieje") 
    else: 
        print("Nie istnieje")