import utils
##   Proszê napisaæ funkcjê, która otrzymuj¹c jako parametr
#wskazuj¹cy na pocz¹tek listy  dwukierunkowej, usuwa z niej
#wszystkie elementy, w których wartoœæ klucza w zapisie
#binarnym ma  nieparzyst¹ iloœæ jedynek.

def bin_count(n):
    count = 0
    while n !=0:
        count+=n%2
        n//=2

    return count % 2 == 1 # zwraca true jezeli nieparzysta ilosc jedynek

def remove_interesting(collection):
    if collection.next == None: # jezeli lista pusta to pomin
        return

    while collection.next!= None: # jezeli nastepny nie jest pusty
        if bin_count(collection.next.value): # sprawdz czy wartos ma nieparzysta ilosc 1 w zapisie bin
            if collection.next.next != None: # jezeli nastepny element nie jest ostani
                collection.next.next.prev = collection # zmodyfikuj jego odwolanie do poprzedniego elementu
            collection.next = collection.next.next # pomin sprawdzany element
        else:
            collection = collection.next # przejdz do nastepnego

def program():
    collection = utils.collection2()
    for i in range(10):
        collection.append(i+1)
    collection.print()
    collection.print_rev()
    print("--")
    remove_interesting(collection)
    collection.print()
    collection.print_rev()