import math
import utils

# Problem wież w Hanoi (treść oczywista)

def hanoi(n, A, B, C):
    if n == 1:
        print(A, "->", B)
    else:
        hanoi(n-1, A, C, B)
        print(A, "->", B)
        hanoi(n-1, C, B, A)


def program():
    hanoi(5,"A","B","C")