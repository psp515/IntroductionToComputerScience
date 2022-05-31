import utils
#  Napis s1 poprzedza napis s2 je¿eli ostatnia litera s1 jest „mniejsza” od pierwszej
#  litery s2. Wed³ug tej zasady rozmieszczono napisy w liœcie cyklicznej, na przyk³ad:
#  ??bartek??leszek??marek??ola??zosia??
# ???????????????????????????
# Proszê napisaæ stosowne definicje typów oraz funkcjê wstawiaj¹c¹ do
# listy napis z zachowaniem zasady poprzedzania. Do funkcji nale¿y przekazaæ
# wskaŸnik do listy oraz wstawiany napis, funkcja powinna zwróciæ wartoœæ logiczn¹ wskazuj¹c¹,
# czy uda³o siê wstawiæ napis do listy. Po wstawieniu elementu wskaŸnik do listy powinien
# wskazywaæ na nowo wstawiony element.

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