# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def task_info():
    print('Программа составляет список простых множителей числа N')

def list_natural_number(num):
    i = 2 
    lst = []
    old = num
    while i <= num:
        if num % i == 0:
            lst.append(i)
            num //= i
            i = 2
        else:
            i += 1
    print(f"Простые множители числа {old} приведены в списке: {lst}")

task_info()
num = int(input("Введите число: "))
list_natural_number(num)