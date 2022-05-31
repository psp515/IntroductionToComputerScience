n = int(input("n="))
a = 1 
b = 1 
while a * b < n:
    c = a + b 
    a = b 
    b = c 
if a*b == n: 
    print("Jest")
else:
    print("Nie jest")