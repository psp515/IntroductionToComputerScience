import utils
##  Napisaæ funkcjê zamieniaj¹c¹ i wypisuj¹c¹
#liczbê naturaln¹ na system o podstawie 2-16.

def calculate_to_system(system, n):
    new_number = []
    system_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while n > 0:
        new_number.append(system_chars[n % system])
        n //= system
    return new_number[::-1]

def program():
    n = utils.get_number()
    for system in range(2, 16+1):
        print(f"System{system}", calculate_to_system(system, n))