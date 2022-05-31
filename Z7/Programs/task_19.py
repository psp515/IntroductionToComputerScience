import utils
# Elementy w li�cie s� uporz�dkowane wed�ug warto�ci
#klucza. Prosz� napisa� funkcj� usuwaj�c� z listy  elementy o
#nieunikalnym kluczu. Do funkcji przekazujemy wskazanie na
#pierwszy element listy,  funkcja powinna zwr�ci� liczb�
#usuni�tych element�w.

def remove_non_uniq(collection):
    if collection.next == None:
        return 0
    count = 0
    while collection.next != None and collection.next.next != None:
        if collection.next.value == collection.next.next.value: # jezeli wartosci sie r�wnaja
            collection.next = collection.next.next # pomin element
            count += 1 # powieksz licznik usunietych element�w
        else:
            collection = collection.next # przejdz do nastpnego elementu

    return count # liczba usunietych element�w


def program():
    collection = utils.collection()
    for i in range(10):
        collection.append(i)
        collection.append(i)

    collection.print()
    print("----")
    print(remove_non_uniq(collection))
    collection.print()