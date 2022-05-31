import task_6
import utils
import random

# Proszê napisaæ funkcjê usuwaj¹c¹ ostatni element listy.
# Do funkcji nale¿y przekazaæ wskazanie na  pierwszy element
# listy.

def remove_last(list):
    if list.next == None:
        return

    prev_element = list # przedostatni element listy
    while list.next != None: # przejdz na koniec listy
        prev_element = list
        list = list.next
    prev_element.next = None  # usun ostatni element



def program():
    my_list = utils.collection()
    for i in range(1):
        task_6.append(my_list, random.randint(1, 420))

    my_list.print()
    print("---------")
    remove_last(my_list)
    my_list.print()