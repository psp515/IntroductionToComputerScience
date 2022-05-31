import utils
# Dana jest lista, który zakoñczona jest cyklem. Napisaæ
#funkcjê, która zwraca liczbê elementów przed  cyklem.

def is_in_series(item, collection):
    count = 0
    while collection.next != None:
        if collection.next == item:
            count += 1
        if count == 2:
            break
        collection = collection.next

    return count>=2


def coll_count(collection):
    first = collection
    count = 0
    while collection.next != None:
        if is_in_series(collection.next, first):
            break
        count+=1
        collection = collection.next

    return count

def program():
    coll = utils.collection()
    series = utils.series(1)
    for i in range(10):
        coll.append(i)
        series.append(i)

    coll.next = series
    print(coll_count(coll))