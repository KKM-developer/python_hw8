import csv
import os.path
import wiew
import log

id_process = 1

def number_of_school(number_school):
    log.log(id_process)
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if number_school == item[1]:
                    wiew.answer(item)
                    count += 1
            if count == 0:
                wiew.answer(f'{number_school} не найден!')
    else:
        wiew.answer('Файл не найден!')

def find_surname(surname):
    log.log(id_process)
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if surname == item[2]:
                    wiew.answer(item)
                    count += 1
            if count == 0:
                wiew.answer(f'{surname} не найден!')
    else:
        wiew.answer('Файл не найден!')


def find_name(name):
    log.log(id_process)
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if name == item[3]:
                    wiew.answer(item)
                    count += 1
            if count == 0:
                wiew.answer(f'{name} не найден!')
    else:
        wiew.answer('Файл не найден!')


def find_class(Number_of_class):
    log.log(id_process)
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if Number_of_class == item[4]:
                    wiew.answer(item)
                    count += 1
            if count == 0:
                wiew.answer(f'Ученик {Number_of_class} класса не найден!')
    else:
        wiew.answer('Файл не найден!')


def find_id():
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            return int(sum_list[-1][0])
    else:
        return 0

