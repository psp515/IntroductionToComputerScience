a = 1 
b = 1
while a < 1000000:
    a, b = b, a + b
print(a/b)