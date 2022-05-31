import utils
# Dana jest lista, który zakoñczona jest cyklem. Napisaæ
# funkcjê, która zwraca liczbê elementów w cyklu.


def count(series):
    stopper = series # obiekt zatrzymujacy liczenie
    count = 0 if series.value == None else 1
    while series.next != stopper:  # jezeli nastepny obiekt jest inny to iteruj dalej w tym wypadku czekamy na wartownika
        count += 1
        series = series.next

    return count


def program():
    series = utils.series() #wartownik
    series.append(2)
    series.append(3)
    series.print()
    print("---")
    print(count(series))

    series = utils.series(2)  # bez wartownika
    series.append(2)
    series.append(3)
    series.print()
    print("---")
    print(count(series))