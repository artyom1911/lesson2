"""Задача 4: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
Пример 10: 0, 1, 2, 3"""


n = int(input("Введите число = "))
i = 0
a = 0
k = 0
while n - 2 ** i > 2 ** (i-1):
    print(k)
    a = 2 ** (i)
    i+=1
    k+=1
