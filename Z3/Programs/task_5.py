import utils
##  Napisaæ program, który wczytuje wprowadzany z
#klawiatury ci¹g liczb naturalnych zakoñczo-nych
#zerem stanowi¹cym wy³¹cznie znacznik koñca danych.
#Program powinien wypisaæ 10 co do wielkoœci
#wartoœæ, jaka wyst¹pi³a w ci¹gu. Mo¿na za³o¿yæ, ¿e
#w ci¹gu znajduje siê wystarczaj¹ca liczba
#elementów.


def program():
    draft = input("Podaj ciag zakonczone bez 0: ")
    numbers = sorted(set(int(i) for i in draft.split())) # stworz zbior posortuj go i ustaw od najwiekszej
    numbers_set = list(numbers) # stworz liste
    print(numbers_set[len(numbers)-10])


