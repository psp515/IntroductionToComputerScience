import utils
# Elementy w liœcie s¹ uporz¹dkowane wed³ug wartoœci
#klucza. Proszê napisaæ funkcjê usuwaj¹c¹ z listy  elementy o
#nieunikalnym kluczu. Do funkcji przekazujemy wskazanie na
#pierwszy element listy,  funkcja powinna zwróciæ liczbê
#usuniêtych elementów.

def remove_non_uniq(collection):
    if collection.next == None:
        return 0
    count = 0
    while collection.next != None and collection.next.next != None:
        if collection.next.value == collection.next.next.value: # jezeli wartosci sie równaja
            collection.next = collection.next.next # pomin element
            count += 1 # powieksz licznik usunietych elementów
        else:
            collection = collection.next # przejdz do nastpnego elementu

    return count # liczba usunietych elementów


def program():
    collection = utils.collection()
    for i in range(10):
        collection.append(i)
        collection.append(i)

    collection.print()
    print("----")
    print(remove_non_uniq(collection))
    collection.print()