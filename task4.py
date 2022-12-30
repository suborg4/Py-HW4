# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def task_info():
    print('Программа формирует случайным образом список коэффициентов')
    print('(значения от 0 до 100)многочлена и записывает в файл многочлен степени k')

def write_file(st):
    with open('file.txt', 'w') as data:
        data.write(st)

def rand():
    return random.randint(0, 101)

def create_mn(k):
    list = [rand() for i in range(k + 1)]
    return list

def creat_str(sp):
    list = sp[::-1]
    vr = ''
    if len(list) < 1:
        vr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                vr += f'{list[i]}x^{len(list)-i-1}'
                if list[i+1] != 0:
                    vr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                vr += f'{list[i]}x'
                if list[i+1] != 0:
                    vr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                vr += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                vr += ' = 0'
    return vr

task_info()
k = int(input("Введите натуральную степень k = "))
ratio = create_mn(k)
write_file(creat_str(ratio))