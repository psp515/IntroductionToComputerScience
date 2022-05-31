s = int(input("s=")) 
a = 1.0
while abs(a*a*a-s) > 0.000001:
    a = (s/(a*a) + 2*a)/3
print(a)