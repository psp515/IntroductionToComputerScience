import utils
import task_6
import random
##   Dana jest niepusta lista, proszê napisaæ funkcjê
#usuwaj¹c¹ co drugi element listy. Do funkcji nale¿y
#przekazaæ wskazanie na pierwszy element listy.

def remove_mod2(list):
    if list.next == None:
        return

    list = list.next # pierwszy element listy nie ma wartosci wiec skip
    while list.next != None:
        tmp = list.next.next # zapisz element 2 dalej
        list.next = tmp # pomin nastepny element w liscie
        if list.next != None: # jezeli nastepny element istnieje
            list = list.next # przejdz do niego

def program():
    my_list = utils.collection()
    for i in range(11):
        task_6.append(my_list, random.randint(1, 420))

    my_list.print()
    print("---------")
    remove_mod2(my_list)
    my_list.print()