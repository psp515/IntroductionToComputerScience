import utils
##   Zastosowanie listy odsy³aczowej do implementacji tablicy
# rzadkiej. Proszê napisaæ trzy funkcje:
# – inicjalizuj¹c¹ tablicê,
# – zwracaj¹c¹ wartoœæ elementu o indeksie n,
# – podstawiaj¹c¹ wartoœæ value pod  indeks n.


class SimpleList():
    def __init__(self, i=-1, value=0): # inicjalizacja tablicy
        self.value = value
        self.i = i
        self.next = None

    def get_by_index(self, index):

        if self.i == index: # jezlie znalazes wartos to ja zwroc
            return self.value

        if self.next == None: # jezeli nie znalazles indexu to error
            raise IndexError

        return self.next.get_by_index(index) # zwroc wartosc

    def insert(self, index, new_value):
        if self.i == index: # jezeli znalazles index to go ustaw i wyjdz z ustawiania
            self.value = new_value
            return

        if self.next == None: # jezeli nie ma nastepnego indexu to go stworz
            self.next = SimpleList(self.i+1, None)

        self.next.insert(index, new_value) # przejdz do nastepnego indexu

    def print(self):
        item = self
        while item.next != None:
            print(item.next.i, item.next.value)
            item = item.next



def program():
    my_list = SimpleList()
    my_list.insert(1, 5)
    my_list.insert(2,5)
    my_list.insert(5,10)

    my_list.print()

    print("Value at 4:",my_list.get_by_index(4))

    print(my_list.get_by_index(10)) # gives index error