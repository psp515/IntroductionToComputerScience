def check(n):
    if n < 2:
        return False 
    if n == 2 or n == 3:
        return True 
    if n%2 == 0:
        return False
    a = 3 
    while a * a <= n:
        if n%a == 0:
            return False 
        a += 2 
    return True 

if check(int(input("n="))) == True:
    print("Jest pierwsza")
else:
    print("Nie jest pierwsza")