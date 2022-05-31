import utils
# Napisz program wczytujący liczbę naturalną z klawiatury
# i odpowiadający na pytanie, czy liczba naturalna jest
# palindromem, a następnie czy jest palindromem w
# systemie dwójkowym

def reverse_bits(bytes):
    new_bytes = ""
    for i in range(len(bytes)):
        new_bytes = bytes[i] + new_bytes
    return new_bytes

def reverse_dec_number(n): # 12
    reversed_number = 0
    while n > 0: # pass # pass # stop
        last_digit = n % 10  # 2 # 1
        n = n // 10 # 1 # 0
        reversed_number = reversed_number*10+last_digit # 0*10 + 2 # 2 * 10 + 1

    return reversed_number # 21

def is_dec_palindrome(n):
    return n == reverse_dec_number(n)

def is_bits_palindrome(n):
    bytes = bin(n)[2:]
    return bytes == reverse_bits(bytes)

def program():
    n = utils.get_number("Podaj liczbe: ")
    a = is_dec_palindrome(n)
    b = is_bits_palindrome(n)
    print("Dec palindrome:", a)
    print("Bits palindrome:", b)
