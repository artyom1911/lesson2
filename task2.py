"""Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите 
минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть."""


a = int(input("Введите колличество арбузов ="))

c = 0
d = 0
for i in range(a):
    wtrmln = int(input('Введите массу арбуза = '))

    if wtrmln > c :
        c = wtrmln

    if wtrmln < d or d == 0 :
        d = wtrmln

print("Для себя", c)
print("Для для тещи", d)
