import utils
##   Dane s� dwie niepuste listy, z kt�rych ka�da zawiera
#niepowtarzaj�ce si� elementy. Elementy w  pierwszej li�cie
#s� uporz�dkowane rosn�co, w drugiej elementy wyst�puj� w
#przypadkowej  kolejno�ci. Prosz� napisa� funkcj�, kt�ra z
#dw�ch takich list stworzy jedn�, w kt�rej uporz�dkowane
#elementy b�d� stanowi� sum� mnogo�ciow� element�w z list
#wej�ciowych. Do funkcji nale�y  przekaza� wskazania na obie
#listy, funkcja powinna zwr�ci� wskazanie na list� wynikow�.
#Na przyk�ad  dla list: 2 -> 3 -> 5 ->7-> 11 8 -> 2 -> 7 -> 4
#powinna pozosta� lista: 2 -> 3 -> 4 -> 5 ->7-> 8 -> 11
def program():
    n = utils.get_number()