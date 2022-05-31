import utils
#  Prosz� napisa� funkcj�, kt�ra dla podanej listy
# odsy�aczowej odwraca kolejno�� jej element�w.

def reverse(collection = utils.collection()):
    if collection.next == None: #jezli lista pusta
        return #koniec

    first = collection #zapisz poaczatek listy
    my_new_list = utils.collection() #stw�rz nowa liste

    while collection.next != None:
        my_new_list.push_front(collection.next.value) # dodaj stary element an poczatek nowej listy
        collection = collection.next # przejdz dalej

    first.next = my_new_list.next # przypisz do poczatku listy nowa liste



def program():
    collection = utils.collection()
    for i in range(10):
        collection.append(i)
    collection.print()
    print("----")
    reverse(collection)
    collection.print()
