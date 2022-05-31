import utils
##    Zaimplementuj zbiór mnogoœciowy liczb naturalnych
#korzystaj¹c ze struktury listy odsy³aczowej.
# - czy  element nale¿y do zbioru
# - wstawienie elementu do zbioru
# - usuniêcie elementu ze zbioru

class multi_set():
    def __init__(self):
        self.value = 0
        self.guardian = True
        self.next = None

    def contains(self, item):

        if self.next == None: # jestem na koncu listy
            return self.value == item # porownaj ostatnie elementy
        if item == self.value: # sprawdz czy wartosci sa rowne i zwroc true jezli tak
            return True

        return self.next.contains(item) # zobacz co sie dzieje dla nastepnego elementu

    def delete(self, value):
        if self.next.next == None:  # jezeli jestes prawie na koncu to
            if self.next.value == value: # sprawdz czy ostatnia wartosc jest do usuniecia
                self.next = None # jezeli tak usun
            return
        if self.next.value == value: # jezeli znalzles element to usun go
            self.next = self.next.next
            return

        self.next.delete(value) # sprawdz dla nastepnego elementu

    def add(self, new_value):

        if self.contains(new_value): # jezlie element w zbiorze nie dodawaj
            return

        object = self
        while object.next != None: # przejdz na koneic zbioru
            object = object.next

        object.next = multi_set(new_value) # dodaj nowy obiekt
        return

    # proste rekurencyjne wysiwetlanie zbioru
    def print_set(self):
        print("Value: ", self.value, "Next: ", self.next)

        if self.next!= None:
            self.next.print_set()


def program():
    # minus tego rozwiazania nie da sie usunac pierwszego elementu
    my_set = multi_set(5)
    my_set.add(10)
    my_set.add(10)
    my_set.add(20)
    my_set.add(21)
    my_set.add(22)
    my_set.add(23)
    my_set.print_set()

    my_set.delete(22)
    my_set.print_set()

