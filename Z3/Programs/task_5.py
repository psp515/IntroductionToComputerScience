import utils
##  Napisa� program, kt�ry wczytuje wprowadzany z
#klawiatury ci�g liczb naturalnych zako�czo-nych
#zerem stanowi�cym wy��cznie znacznik ko�ca danych.
#Program powinien wypisa� 10 co do wielko�ci
#warto��, jaka wyst�pi�a w ci�gu. Mo�na za�o�y�, �e
#w ci�gu znajduje si� wystarczaj�ca liczba
#element�w.


def program():
    draft = input("Podaj ciag zakonczone bez 0: ")
    numbers = sorted(set(int(i) for i in draft.split())) # stworz zbior posortuj go i ustaw od najwiekszej
    numbers_set = list(numbers) # stworz liste
    print(numbers_set[len(numbers)-10])


