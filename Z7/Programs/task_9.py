import utils
import task_6
import random
##   Dana jest niepusta lista reprezentuj¹ca liczbê
#naturaln¹. Kolejne elementy listy przechowuj¹ kolejne
#cyfry. Proszê napisaæ funkcjê zwiêkszaj¹c¹ tak¹ liczbê o 1.

class collection():
    def __init__(self, new_value=-1): # przechowywane wartosci
        self.value = new_value
        self.next = None

    def print(self):
        if self.next != None:
            val = self.next
            while val.next != None:
                print(val.value,end="")
                val = val.next

            print(val.value)

def increase(list):
    def increase_2(list):
        if list.next != None: # przejdz na koniec listy
            up = increase_2(list.next)

        if list.next == None: # na koncu listy
            list.value += 1 #dodaj 1
            upcount = list.value // 10
            list.value = list.value % 10
            return upcount # zwroc czy zwieksza sie liszba setek jednosc dezsiatek itd

        if up != None and list.value!=-1: # jezeli nie jestes na poaczatku ani na koncu listy
            list.value += up # powiekszaj lcizbe dziesiatek setek itd
            up = list.value // 10
            list.value = list.value % 10
        return up # zwracaj czy kolejna liczba rosnie

    v = increase_2(list) # powieksz liste o 1
    if v == 1: # jezeli tutaj wpada jedynka to znaczy ze postaje liczba z 1 cyfra wiecej dla 999 to 1000 itd
        append_front(list, 1)


def append_front(list, value):
    item = collection(value)
    item.next = list.next
    list.next = item

def program():
    my_list = collection()
    for i in range(3):
        append_front(my_list, random.randint(1, 9))
    my_list.print()
    increase(my_list)
    print("----")
    my_list.print()