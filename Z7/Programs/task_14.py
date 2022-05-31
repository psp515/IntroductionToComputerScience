import utils
##   Proszê napisaæ funkcjê, otrzymuj¹c¹ jako parametr
#wskaŸnik na pierwszy element listy o wartoœciach  typu int,
#usuwaj¹c¹ wszystkie elementy, których wartoœæ dzieli bez
#reszty wartoœæ bezpoœrednio  nastêpuj¹cych po nich
#elementów.

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