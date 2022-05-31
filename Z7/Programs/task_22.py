import utils
# Dana jest lista, który byæ mo¿e zakoñczona jest cyklem.
# Napisaæ funkcjê, która sprawdza ten fakt


def is_series(collection):
    stopper = collection
    while collection.next != None: # jezeli nie ma konca tablic iteruj
        if collection.next == stopper: # jezeli spotakles pierwszy element to jest to cykl
            return True
        collection = collection.next # przejdz do nastepnego elemtentu

    return False



def program():
    coll = utils.collection()
    series = utils.series()
    for i in range(10):
        coll.append(i)
        series.append(i)

    print("Series", is_series(series))
    print("Coll:", is_series(coll))

