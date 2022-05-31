import utils
# Zbiór mnogoœciowy zawieraj¹cy napisy jest
#reprezentowany w postaci jednokierunkowej listy. Napisy  w
#³añcuchu s¹ uporz¹dkowane leksykograficznie. Proszê napisaæ
#stosowne definicje typów oraz  funkcjê dodaj¹c¹ napis do
#zbioru. Do funkcji nale¿y przekazaæ wskaŸnik do listy oraz
#wstawiany napis,  funkcja powinna zwróciæ wartoœæ logiczn¹
#wskazuj¹c¹, czy w wyniku operacji moc zbioru uleg³a  zmianie

class stringset():
    def __init__(self, new_value=None):
        self.value = new_value
        self.next = None

    def add_string(self, new_value):
        if self.next == None: #jezeli nie ma jeszcze zadnej wartosci w liscie
            self.next = stringset(new_value) #dodaj wartosc
            return True #true bo lista sie powieksza

        item = self
        while item.next != None: #iterujemy do momentu gdy spotakmy element none
            val = item.next.value #pobieramy wartosc
            if new_value == val: #sprawdzamy czy sa takie same
                return False #jezeli tak to nie dodajemy i zwracamy false bo dlugosc sie nie zmienia
            if new_value == min(val, new_value): #sprawdzamy porzadek leksykograficzny
                tmp = item.next #zapisujemy dalsza czesc listy
                item.next = stringset(new_value) #dodajemy element
                item.next.next = tmp #ustawiamy ciag dalszy listy
                return True #wielkosc sie zmienia

            item = item.next


        item.next = stringset(new_value) # jezeli spotaklismy none to nie znalezlismy takiego samego elemntu => dodajemy na koniec
        return True #wielkosc sie zmienia

    def append(self, new_value):
        if self.next == None:
            self.next=stringset(new_value)
            return

        self.next.append(new_value)
    def print(self):
        if self.next != None:
            val = self.next
            while val.next != None:
                print(val.value,end=",")
                val = val.next

            print(val.value)


def program():
    item = stringset()
    item.add_string("asa")
    item.add_string("asd")
    item.add_string("asc")
    item.add_string("ase")
    item.add_string("as")
    print(item.get_len())
    item.print()
    print(item.add_string("asb"))
    item.print()
    print(item.add_string("asb"))
    item.print()