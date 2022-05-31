import random

import utils
##   Proszê napisaæ funkcjê scalaj¹c¹ dwie posortowane listy
#w jedn¹ posortowan¹ listê. Do funkcji nale¿y  przekazaæ
#wskazania na pierwsze elementy obu list, funkcja powinna
#zwróciæ wskazanie do scalonej  listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.

def glue_it(coll1, coll2):
    if coll1.next == None: # jezli jedna lista pusta to zwroc druga
        return coll2
    if coll2.next == None: # jezli jedna lista pusta to zwroc druga
        return coll1

    collection = utils.collection()
    while coll1.next != None or coll2.next != None: # sprawdzaj czy skonczyles iterowac
        if coll1.next != None and (coll2.next == None or (coll1.next.value <= coll2.next.value)): #jezeli te warunki sa
            collection.append(coll1.next.value)# spelnione na pewno mozemy dodac element z pierwszej listy
            coll1 = coll1.next
        else:
            collection.append(coll2.next.value) #dodaj z drugiej listy
            coll2 = coll2.next

    return collection

def glue_rek(coll1, coll2,is_first = True):
    if coll1.next == None and coll2.next == None: # jezlei przeszedles obie listy koniec
        return None

    if is_first: # jezeli zaczynasz
        collection = utils.collection() # stworz wartownika
        collection.next = glue_rek(coll1, coll2, False) # zaznij ³aczyc liste
        return collection

    if coll1.next != None and (coll2.next == None or (coll1.next.value <= coll2.next.value)): # jezeli spelnione
        collection = utils.collection(coll1.next.value) # stworz nowa klase z wartoscia
        collection.next = glue_rek(coll1.next, coll2, False) # znajdz nastepny element
        return collection # zwróc
    else:
        collection = utils.collection(coll2.next.value)  # stworz nowa klase z wartoscia
        collection.next = glue_rek(coll1, coll2.next, False)  # znajdz nastepny element
        return collection # zwróc


def program():
    coll1 = utils.collection()
    coll2 = utils.collection()
    a=0
    b=0
    for i in range(3):
        a1 = random.randint(a,1000)
        b1 = random.randint(b,1000)
        a, b = a1,b1
        coll1.append(a1)
        coll2.append(b1)

    coll2.print()
    coll1.print()
    new_list = glue_it(coll1, coll2)
    print("---")
    lista = glue_rek(coll1,coll2)
    print(lista.print()==new_list.print())