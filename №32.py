"""Задача 32: 
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)"""

list_1 = []
result = []
max = 15
min = 3
i = 0
for i in range(int(input('Количество элементов: '))):
    list_1.append(int(input('Введите число: ')))
print(list_1)   
for num in list_1: 
    if num <= max: 
        if num >= min:
            print(num)
            result.append(num)
print(result)
