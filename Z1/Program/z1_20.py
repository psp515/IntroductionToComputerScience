def sqrt(s):
    n = 1.0 
    while abs(n*n-s) > 0.00001:
        n = (s/n + n)/2.0 
    return n 
a = float(input("a="))
b = float(input("b=")) 

for i in range (0,20):
    at = a 
    bt = b 
    a = sqrt(at * bt) 
    b = (at+bt)/2 

print(a)
print(b)