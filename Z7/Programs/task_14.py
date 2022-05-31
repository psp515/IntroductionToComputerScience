import utils
##   Prosz� napisa� funkcj�, otrzymuj�c� jako parametr
#wska�nik na pierwszy element listy o warto�ciach  typu int,
#usuwaj�c� wszystkie elementy, kt�rych warto�� dzieli bez
#reszty warto�� bezpo�rednio  nast�puj�cych po nich
#element�w.

def remove_modn(collection, value):
    if collection.next == None:
        return

    while collection.next != None: # jezei ostani element jest rozny od None
        if collection.next.value % value == 0: # jezeli liczby sie dziela
            collection.next = collection.next.next # pomin liczbe w kolekcji
        else:
            collection = collection.next #idz do nastepnego elementu






def program():
    collection = utils.collection()
    collection.append(10)
    collection.append(5)
    collection.append(10)
    collection.append(6)
    collection.append(7)
    collection.append(8)
    collection.append(8)
    collection.append(9)
    collection.print()
    print("--")
    remove_modn(collection,2)
    collection.print()