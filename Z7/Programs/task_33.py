import utils
#  Napis s1 poprzedza napis s2 je�eli ostatnia litera s1 jest �mniejsza� od pierwszej
#  litery s2. Wed�ug tej zasady rozmieszczono napisy w li�cie cyklicznej, na przyk�ad:
#  ??bartek??leszek??marek??ola??zosia??
# ???????????????????????????
# Prosz� napisa� stosowne definicje typ�w oraz funkcj� wstawiaj�c� do
# listy napis z zachowaniem zasady poprzedzania. Do funkcji nale�y przekaza�
# wska�nik do listy oraz wstawiany napis, funkcja powinna zwr�ci� warto�� logiczn� wskazuj�c�,
# czy uda�o si� wstawi� napis do listy. Po wstawieniu elementu wska�nik do listy powinien
# wskazywa� na nowo wstawiony element.

class NameClass():
    def __init__(self, value=None, next = self):
        self.value = None
        self.next = next

    def append(self, value):
        if self.next == None:
            self.next = NameClass(value, self)
            return

        start = self
        if self.value == None: # pomijanie wartownika
            self = self.value

        first, last = value[0], value[-1]
        while start != self:
            if self.value[0] < last:



def program():
    n = utils.get_number()