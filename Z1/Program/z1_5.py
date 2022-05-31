s = float(input("s="))
a = 1.0
while abs(a*a-s) > 0.00001:
    a = (s/a + a)/2
print(a)