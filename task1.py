# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

def task_info():
    print('Программа вычисляет число c заданной точностью d,')

def calculation_pi(d):
    d = d[2:len(d)]
    print(round(math.pi,len(d)))

task_info()
d = input('Введите число для заданной точности числа Пи: ')
calculation_pi(d)