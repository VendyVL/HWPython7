
from write_numbers import Write_num
from search_number import Searching
from delete_user import Deleting
from print_all import Printing

def doing():
    print('1 - добавить номер')
    print('2 - найти номер')
    print('3 - посмотреть всех')
    print('4 - удалить пользователя')

    doing = input('Выберите действие: ')

    if doing == '1': Write_num()
    elif doing == '2':Searching()
    elif doing == '3':Printing()
    elif doing == '4':Deleting()
    else: print('Ошибка')