import random

import utils
#Prosz� napisa� funkcj� wstawiaj�c� na koniec listy nowy
#element. Do funkcji nale�y przekaza�  wskazanie na pierwszy
#element listy oraz wstawian� warto��.

def append(list, new_value):

    while list.next != None: # przejdz na koniec listy
        list = list.next

    list.next = utils.collection(new_value) # dodaj obiekt do listy

def program():
    my_list = utils.collection()
    for i in range(10):
        append(my_list,random.randint(1,420))

    my_list.print()