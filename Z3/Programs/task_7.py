import utils
import random
##  Napisaæ program wype³niaj¹cy N-elementow¹
#tablicê t liczbami naturalnymi 1-1000 i spraw-
#dzaj¹cy czy istnieje element tablicy zawieraj¹cy
#wy³¹cznie cyfry nieparzyste.

def has_valid_digit(element = 0):
    while element > 0:
        if element % 2 == 0: # sprawdzam ostatni element
            return False
        element //= 10
    return True

def validate_array(arr = []):
    for el in arr:
        if has_valid_digit(el) == False:
            return False
    return True

def program():
    n = utils.get_number()
    print(validate_array(utils.random_array(n,0,10)))