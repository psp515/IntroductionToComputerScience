import math
import utils

# Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę
# samą liczbę sa- mogłosek oraz sumy kodów ascii liter z których są zbudowane są
# identyczne, na przykład ′′ula′′ → 117, 108, 97 oraz ′′ exe′′ → 101, 120, 101.
# Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowa-
# nie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo
# funkcja powinna wypisać znaleziony wyraz.

def count_vowels_and_ascii_sum(s):
    v_counter = 0
    a_counter = 0
    for a in s:
        if any(a == e for e in ['a','e','i','o','u','y']):
            v_counter+=1
        a_counter += ord(a)

    return v_counter, a_counter

def get_letters(s="", arr_len=0, mask=0):
    arr = [False for _ in range(arr_len)]
    i = 0
    while mask > 0:
        if mask % 2 == 1:
            arr[i] = True
        mask //= 2
        i += 1

    new_str = ""
    for j in range(arr_len):
        if arr[j] == True:
            new_str += s[j]

    return new_str

def task(s1,s2, mask=1):
    def rec_s2(s1, s2, mask=1):
        if mask >= 2 ** len(s2):
            return
        new_s2 = get_letters(s2, len(s2), mask)
        if count_vowels_and_ascii_sum(s1) == count_vowels_and_ascii_sum(new_s2):
            print("Examples: ", s1, new_s2)
            return True
        rec_s2(s1, s2, mask+1)

    if mask >= 2**len(s1):
        return

    new_s1 = get_letters(s1,len(s1), mask)
    if rec_s2(new_s1, s2, 0):
        return
    task(s1, s2, mask + 1)

def program():
    task("alu", "eex")

