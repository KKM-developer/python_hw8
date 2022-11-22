import export_data as exp
import import_data as imp
import wiew
import log

def button_click():
    wiew.hello()
    choise = wiew.button()
    while choise != 'q':
        if choise == '1':
            exp.export_data()
        elif choise == '2':
            what_find = input('Для поиска по фамилии введите "1"\nДля поиска по имени введите "2"\nДля поиска по номеру класса введите "3"\nДля поиска по номеру школы введите "4"\n')
            if what_find == '1': imp.find_surname(input('Введите фамилию: '))
            if what_find == '2': imp.find_name(input('Введите имя: '))
            if what_find == '3': imp.find_class(input('Введите класс: '))
            if what_find == '4': imp.number_of_school(input('Введите номер школы: '))


        choise = wiew.button()

