import utils
##  Napisa? program wyznaczaj?cy na drodze
#eksperymentu prawdopodobie?stwo tego, ?e w grupie
#N przypadkowo spotkanych os?b, co najmniej dwie
#urodzi?y si? tego samego dnia roku. Wyznaczy?
#warto?ci prawdopodobie?stwa dla N z zakresu 20-40.
#1

def probability(n):
    p_prim = 1
    for i in range(n):
        p_prim *= (365 - i) / 365
    return 1 - p_prim

def program():
    for i in range(20, 41):
        print(f"{i} Propability: ", probability(i))