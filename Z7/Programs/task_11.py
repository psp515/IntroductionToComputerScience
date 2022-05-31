import utils
##   Lista zawiera niepowtarzaj�ce si� elementy. Prosz�
#napisa� funkcj� do kt�rej przekazujemy wska�nik  na pocz�tek
#oraz warto�� klucza. Je�eli element o takim kluczu wyst�puje
#w li�cie nale�y go usun�� z  listy. Je�eli elementu o
#zadanym kluczu brak w li�cie nale�y element o takim kluczu
#wstawi� do listy.

class collection():
    def __init__(self, new_key=None): # przechowywane wartosci
        self.key = new_key
        self.next = None

    def append(self, new_key):
        if self.next == None:
            self.next = collection(new_key)
            return

        self.next.append(new_key)

    def print(self):
        if self.next != None:
            val = self.next
            while val.next != None:
                print(val.key,end=",")
                val = val.next

            print(val.key)

    def weird_add(self, new_key):
        item = self
        while item.next != None: # iteruj do konca listy
            if item.next.key == new_key: # jezeli znalazles klucz
                item.next == item.next.next # pomin element z kluczem
                return
            item = item.next # przejdz do nastepego elementu

        item.next = collection(new_key) # dodaj element

def program():
    my_list = collection()
    for i in range(10):
        my_list.append(i)
    my_list.print()
    print("--")
    my_list.weird_add(0)
    my_list.print()
    print("--")
    my_list.weird_add(9)
    my_list.print()
    print("--")
    my_list.weird_add(124)
    my_list.print()
    print("--")
