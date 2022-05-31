import utils
##   Prosz� napisa� funkcj�, kt�ra otrzymuj�c jako parametr
#wskazuj�cy na pocz�tek listy  jednokierunkowej, usuwa z niej
#wszystkie elementy, w kt�rych warto�� klucza w zapisie
#tr�jkowym  ma wi�ksz� ilo�� jedynek ni� dw�jek.

def has_more_ones(n): # proste zliaczanie  czy w liczbie jest wiecej 1 czy 2
    count_1 = 0
    count_2 = 0
    while n != 0:
        val = n%3
        n //= 3
        if val == 2:
            count_2+=1
        if val == 1:
            count_1+=1

    return count_1 > count_2 #

def delete_item(collection):
    if collection.next == None: # pusta lista => pomin
        return

    while collection.next != None: # jezeli nie jestes na koncu list to sprawdzaj
        if has_more_ones(collection.next.value): #jezeli ma wiecej jedynek
            collection.next = collection.next.next # pomin element
        else:
            collection = collection.next # przejdz do nastepnego elementu


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
    delete_item(collection)
    collection.print()
