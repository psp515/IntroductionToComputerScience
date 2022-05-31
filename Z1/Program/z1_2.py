w1 = 1
w2 = 1
while w2 <= 2021:
    a = w1
    b = w2
    while a < 2021:
        c = a + b
        a = b 
        b = c 
    if a == 2021: 
        print(str(w1) + " " + str(w2))
        break
    if w1 == w2: 
        w2 += 1 
        w1 = 1 
    else: 
        w1 += 1