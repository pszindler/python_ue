import string
import random as rnd

data_list = [1, 2, 3, 4, 5.0, 6.0, 7.1, 8.1, True, False, True, False, 'a',
            'b', 'c', 'd', 'e']

x = rnd.choices(data_list, k=20)

# dopisac funkcje ktora tworzy nowa liste, nowa lista zawiera 4 listy ktore posiadaja poukladane typy danych. 
