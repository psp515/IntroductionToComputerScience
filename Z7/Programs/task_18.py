import utils
##   Proszê napisaæ funkcjê, która pozostawia w liœcie
#wy³¹cznie elementy unikalne. Do funkcji nale¿y  przekazaæ
#wskazanie na pierwszy element listy.

def could_be_added(collection, value): # sprawdz czy w nowej liscie jest taki sam element
    while collection.next !=None:
        if collection.next.value == value:
            return False # jezeli jest
        collection = collection.next
    return True # jezeli nie ma


def remove_copy(collection):
    first = collection
    new_collection = utils.collection() # nowa lista obiektów
    while collection.next != None:
        if could_be_added(new_collection, collection.next.value): # sprawdzam warunek
            new_collection.append(collection.next.value) # dodaje element
        collection = collection.next # przechodze do sprawdzenia nastpengeo

    first.next = new_collection.next # zapisuje nowa liste

def program():
    collection = utils.collection()
    for i in range(10):
        collection.append(i)
    for i in range(10):
        collection.append(i)
    collection.print()
    print("----")
    remove_copy(collection)
    collection.print()