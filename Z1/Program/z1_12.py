a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

while a%b != 0:
    d = a%b 
    a = b 
    b = d 
while b%c != 0:
    d = b%c 
    b = c 
    c = d 
print(c)