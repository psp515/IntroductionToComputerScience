a = 1
b = 5
c = (a+b)/2
while abs(c**c-2020) > 0.0001:
    if c**c > 2020:
        b = c 
    else:
        a = c 
    c = (a+b)/2
print(c)