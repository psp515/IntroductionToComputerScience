import utils
##   Prosz� napisa� funkcj�, kt�ra otrzymuj�c jako parametr
#wskazuj�cy na pocz�tek listy  jednokierunkowej, przenosi na
#pocz�tek listy te z nich, kt�re maj� parzyst� ilo�� pi�tek w
#zapisie  �semkowym.

def has_fife(n): # proste zliaczanie  czy w liczbie jest wiecej 1 czy 2
    count_5 = 0
    while n != 0:
        if n % 8 == 5:
            count_5 += 1
        n //= 8

    return count_5 % 2 == 0

def sort_items(collection):
    if collection.next == None: # pusta lista => pomin
        return

    new_list = utils.collection()
    first = collection # zapisz odnosnik do poczatku listy

    while collection.next != None:
        if has_fife(collection.next.value): # jezeli ma parzysta liczbe 5
            new_list.push_front(collection.next.value) # dodaj na poczatek listy
        else:
            new_list.append(collection.next.value) #dodaj na koniec listy
        collection = collection.next

    first.next = new_list.next


def program():
    print(has_fife(4))
    collection = utils.collection()
    collection.append(10)
    collection.append(7)
    collection.append(5)
    collection.append(5)
    collection.append(5)
    collection.append(5)
    collection.append(5)
    collection.append(9)
    collection.append(5)
    collection.print()
    print("--")
    sort_items(collection)
    collection.print()