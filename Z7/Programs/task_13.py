import utils
##   Prosz� napisa� funkcj�, otrzymuj�c� jako parametr
#wska�nik na pierwszy element listy o warto�ciach  typu int,
#usuwaj�c� wszystkie elementy, kt�rych warto�� jest mniejsza
#od warto�ci bezpo�rednio  poprzedzaj�cych je element�w.


def remove_range(collection, value):
    if collection.next == None: # jezeli pusta lsita
        return  # wyjdz

    copy = collection # zapisz kolekcje
    while copy.next != None and copy.next.value < value: # iteruj po kolekcji do momentu spotaknia konca lub takiesamej/ wiekszej wartosci
        copy = copy.next

    collection.next = copy.next # usun poprzednie elementy

def program(): # zak�adam ze od razu posortuje sobie liste
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