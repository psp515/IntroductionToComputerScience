
class collection():
    def __init__(self, new_value=None): # przechowywane wartosci
        self.value = new_value
        self.next = None

    def append(self, new_value):
        if self.next == None:
            self.next = collection(new_value)
            return
        self.next.append(new_value)

    def push_front(self, val):
        q = collection(val)
        q.next = self.next
        self.next = q

    def add_in_order(self, new_value):
        if self.next == None:
            self.next = collection(new_value)
            return True

        item = self
        while item.next != None:
            val = item.next.value
            if new_value == val:
                return False

            if new_value == min(val, new_value):
                tmp = item.next
                item.next = collection(new_value)
                item.next.next = tmp
                return True

            item = item.next


        item.next = collection(new_value) # jezeli spotaklismy none to nie znalezlismy takiego samego elemntu => dodajemy na koniec
        return True #wielkosc sie zmienia

    def get_len(self):
        if self.value == None and self.next == None:
            return 0

        if self.value == None:
            return self.next.get_len()

        if self.next == None:
            return 1

        return self.next.get_len() + 1

    def print(self):
        if self.next != None:
            val = self.next
            while val.next != None:
                print(val.value,end=",")
                val = val.next

            print(val.value)

class collection2():
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def append(self, value):
        q = self
        while q.next != None:
            q = q.next

        q.next = collection2(value)
        q.next.prev = q

    def print_rev(self):
        if self.next != None:
            val = self.next
            while val.next != None:
                val = val.next
            while val.prev!= None:
                print(val.value, end=",")
                val = val.prev
            print("")

    def print(self):
        if self.next != None:
            val = self.next
            while val.next != None:
                print(val.value, end=",")
                val = val.next

            print(val.value)

class series():
    def __init__(self, value = None):
        self.value = value
        self.next = self

    def append(self, value):
        q = series(value)
        q.next = self.next
        self.next = q

    def print(self):
        stopper = self
        while self.next != stopper:
            print( self.next.value, end=",")
            self = self.next

        print(stopper.next.value)
