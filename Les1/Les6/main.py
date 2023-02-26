# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# n = int(input("Введите колчество элементов массива: "))
# a1= int(input("Введите первое число массива: "))
# d = int(input("Введите разность: " ))

# progress = [a1 + (i - 1) * d for i in range(1, n + 1)]
# print(*progress)


# Вариант эталлоного решения
# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
# print(a1 + i * d)


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


# from random import randint
 
# minimum = int(input( "Введите минимальное значение:"))
# maximum = int(input( "Введите максимальное значение:"))
              
# array1 = [randint(1, 10) for _ in range(10)]

# print("Первоначальный массив", array1, sep='\n')

# indexes = [i for i, j in enumerate(array1) if minimum <= j <= maximum]

# print("Индексы массива", indexes, sep='\n')


# Вариант эталонного решения:
#  list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
# if min_number <= list_1[i] <= max_number:
# print(i)
