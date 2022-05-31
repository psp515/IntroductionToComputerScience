import utils
##   Dane s¹ dwie niepuste listy, z których ka¿da zawiera
#niepowtarzaj¹ce siê elementy. Elementy w  pierwszej liœcie
#s¹ uporz¹dkowane rosn¹co, w drugiej elementy wystêpuj¹ w
#przypadkowej  kolejnoœci. Proszê napisaæ funkcjê, która z
#dwóch takich list stworzy jedn¹, w której uporz¹dkowane
#elementy bêd¹ stanowiæ sumê mnogoœciow¹ elementów z list
#wejœciowych. Do funkcji nale¿y  przekazaæ wskazania na obie
#listy, funkcja powinna zwróciæ wskazanie na listê wynikow¹.
#Na przyk³ad  dla list: 2 -> 3 -> 5 ->7-> 11 8 -> 2 -> 7 -> 4
#powinna pozostaæ lista: 2 -> 3 -> 4 -> 5 ->7-> 8 -> 11
def program():
    n = utils.get_number()