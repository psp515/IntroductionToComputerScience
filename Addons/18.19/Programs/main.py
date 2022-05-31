import task1
import task1_b
import task2


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def AnOne(n):
    if n < 3:
        return 1
    if n % 2==0:
        return AnOne(n-3)+ AnOne(n-1)+1
    return (AnOne(n-1) % 7)

if __name__ == '__main__':
    print_hi('PyCharm')
    for i in range(10):
        print(f"{i}: ", AnOne(i))
    #task1.program() #DONE
    #task1_b.program() #DONE
    #task2.program() #DONE
    print("end")