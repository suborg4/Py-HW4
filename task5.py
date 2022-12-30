# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file_1.txt', 'r') as data:
    str1 = data.readlines()
with open('file_2.txt', 'r') as data:
    str2 = data.readlines()
list1 = calc_mn(str1)
list2 = calc_mn(str2)
l = len(list1)
if len(list1) > len(list2):
    l = len(list2)
list3 = [list1[i] + list2[i] for i in range(l)]
if len(list1) > len(list2):
    m = len(list1)
    for i in range(l, m):
        list3.append(list1[i])
else:
    m = len(list2)
    for i in range(l, m):
        list3.append(list2[i])
write_file("file_3.txt", create_str(list3))
with open('file_3.txt', 'r') as data:
    st3 = data.readlines()