def nwd(a,b):
    while a%b != 0:
        c = a%b 
        a = b 
        b = c 
    return b 

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
nww1 = (a*b)/nwd(a,b)
nww2 = (nww1 * c)/nwd(nww1, c)
print(int(nww2))