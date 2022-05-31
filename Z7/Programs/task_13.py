import utils
##   Proszê napisaæ funkcjê, otrzymuj¹c¹ jako parametr
#wskaŸnik na pierwszy element listy o wartoœciach  typu int,
#usuwaj¹c¹ wszystkie elementy, których wartoœæ jest mniejsza
#od wartoœci bezpoœrednio  poprzedzaj¹cych je elementów.


def remove_range(collection, value):
    if collection.next == None: # jezeli pusta lsita
        return  # wyjdz

    copy = collection # zapisz kolekcje
    while copy.next != None and copy.next.value < value: # iteruj po kolekcji do momentu spotaknia konca lub takiesamej/ wiekszej wartosci
        copy = copy.next

    collection.next = copy.next # usun poprzednie elementy

def program(): # zak³adam ze od razu posortuje sobie liste
    collection = utils.collection()
    collection.add_in_order(5)
    collection.add_in_order(5)
    collection.add_in_order(6)
    collection.add_in_order(4)
    collection.add_in_order(2)
    collection.print()
    print("---")
    remove_range(collection, 5)
    collection.print()