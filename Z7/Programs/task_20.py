import utils
##   Dana jest lista zawieraj¹ca ci¹g obustronnie domkniêtych
#przedzia³ów. Krañce przedzia³ów okreœla  uporz¹dkowana para
#liczb ca³kowitych. Proszê napisaæ stosowne deklaracje oraz
#funkcjê redukuj¹c¹  liczbê elementów listy. Na przyk³ad
#lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien
#zostaæ  zredukowany do listy: [13,19] [2,6] [7,12]

class node():
    def __init__(self, min=None, max=None):
        self.next = None
        self.min = min
        self.max = max

    def append(self, min, max):
        if self.next == None:
            self.next = node(min, max)
            return
        self.next.append(min,max)

    def print(self):
        if self.next != None:
            print("(", self.next.min,",", self.next.max, ")", end="|")
            self.next.print()

    def func(self):
        first = self
        new_collection = node()
        new_first = new_collection
        while self.next != None:

            while new_collection.next != None:
                pass

            new_collection = new_first


def program():
    Node = node()
    Node.append(1, 20)
    Node.append(13, 23)
    Node.append(24, 25)
    Node.print()