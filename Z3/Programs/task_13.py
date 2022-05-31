import utils
# Proszê napisaæ program, który wype³nia
# N-elementow¹ tablicê t trzycyfrowymi liczbami
# pseudolosowymi, a nastêpnie wyznacza i wypisuje
# d³ugoœæ najd³u¿szego podci¹gu spójnego znajduj¹ce-
# go siê w tablicy dla którego w tablicy wystêpuje
# równie¿ rewers tego ci¹gu. Na przyk³ad dla
# tablicy: t= [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
# odpowiedzi¹ jest liczba 4.

# dziala ale mozna usprawnic

def rev_arr_contains(rev_arr=[], draft=[]):
    for i in range(len(rev_arr)-len(draft)):
        counter = 0
        for j in range(len(draft)):
            if rev_arr[i+j] == draft[j]:
                counter+=1
        if counter == len(draft):
            return True

    return False

def longest_draft(arr = []):
    rev_arr = arr[::-1]
    max_count = 0
    counter = 0
    act_draft = []
    for i in arr:
        act_draft+=[i]
        counter+=1
        if rev_arr_contains(rev_arr,act_draft) == True:
            if max_count < counter:
                max_count = counter
        else:
            arr_copy = act_draft.copy()
            copy_counter = counter
            for e in arr_copy:
                arr_copy.remove(e)
                copy_counter -= 1
                if len(arr_copy) == 0:
                    break
                if rev_arr_contains(rev_arr, arr_copy) == True:
                    if max_count < copy_counter:
                        max_count = copy_counter


    return max_count

def program():
    n = utils.get_number("Arr len: ")
    print(longest_draft([2,9,3,1,7,11,9,6,7,7,1,3,9,2,12,15]))

