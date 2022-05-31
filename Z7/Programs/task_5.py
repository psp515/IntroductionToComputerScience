import utils
# Prosz� napisa� funkcj�, kt�ra rozdziela elementy listy
# odsy�aczowej do 10 list, wed�ug ostatniej cyfry  pola val. W
# drugim kroku powsta�e listy nale�y po��czy� w jedn� list�
# odsy�aczow�, kt�ra jest  posortowana niemalej�co wed�ug
# ostatniej cyfry pola val.

def split(simplelist = utils.collection()):
    dig_arrays = [utils.collection() for _ in range(10)] # 10 list na podzia�

    while simplelist.next != None:
        last_dig = simplelist.next.value % 10 # ostatnia cyfra liczby
        dig_arrays[last_dig].append(simplelist.next.value) # dodajemy do odpowiedniej listy
        simplelist = simplelist.next # nastepny element

    collection = dig_arrays[0] #tworzymy nowa liste
    first = collection # zapisujeme poaczatek listy
    for i in range(1, 10): # �aczenie list
        while collection.next != None: # przejdz na koniec listy (aby nie uci�ao niektorych kawalkow)
            collection = collection.next
        collection.next = dig_arrays[i].next #dodaj nowa tablice

    return first # zwracam poaczatek lsity



def program():
    collection = utils.collection()
    for i in range(23):
        collection.append(i)
    collection.print()
    collection = split(collection)
    collection.print()