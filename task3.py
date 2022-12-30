# Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

def task_info():
    print('Программа выведет список неповторяющихся элементов')
    print('исходной последовательности')

def non_repeating_elements(lst):
    new_lst = []
    [new_lst.append(i) for i in lst if i not in new_lst]
    print(f"Список из неповторяющихся элементов: {new_lst}")

task_info()
lst = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Начальный список: {lst}")
non_repeating_elements(lst)