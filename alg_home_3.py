__author__ = 'Брызгалова Юлия Викторовна'
print("Домашнее задание №3")
import random

#
# 1. В диапазоне натуральных чисел от 2 до 1000000 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
print ("Задание №1")
def kratn(a):
    colich = 0
    for j in range(2,1000001):
        if j % a == 0:
            colich += 1
    return colich

m2 = [kratn(i) for i in range(2,10)]
print (m2)

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
print()
print ("Задание №2")
m1 = [random.randint(0,100) for i in range(0,10)]
m2 = [i for i in range(0, len(m1)) if m1[i] % 2 == 0]
print ("m1 = ", m1,"    m2 = ", m2)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
print()
print ("Задание №3")
m1 = [random.randint(0,100) for i in range(0,10)]
a = max(m1)
b = m1.index(max(m1))
c = min(m1)
d = m1.index(min(m1))

m1[b] = c
m1[d] = a


# 4. Определить, какое число в массиве встречается чаще всего.
print()
print ("Задание №4")

m1 = [random.randint(0,100) for i in range(0,20)]
m2 = [m1.count(m1[i]) for i in range(0, len(m1))]
print ("Массив: ", m1)
print (" В массиве встречается чаще всего число:  ", m1[m2.index(max(m2))])

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
print()
print ("Задание №5")

m1 = [random.randint(-100,10) for i in range(0,10)]
print ("Массив: ", m1)
print ("Максимальный элемент: ", min(m1), ". Позиция элемента: ", m1.index(min(m1)))

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
print()
print ("Задание №6")

m1 = [random.randint(0,10) for i in range(0,10)]

if m1[m1.index(min(m1))] < m1[m1.index(max(m1))]:
    print (m1, "         ", sum(m1[(m1.index(min(m1))+1):m1.index(max(m1))]))
elif m1[m1.index(min(m1))] == m1[m1.index(max(m1))]:
    print (m1, "         ", 0)
else:
    print (m1, "         ", sum(m1[(m1.index(max(m1))+1):m1.index(min(m1))]))

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
print()
print ("Задание №7")

m1 = [random.randint(0,10) for i in range(0,10)]
print(m1)
print ("Первое число: ", m1[m1.index(min(m1))])
m2 = m1[:]
m2.pop(m2.index(min(m2)))

print ("Второе число: ", m2[m2.index(min(m2))])

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
print()
print ("Задание №8")

# m = 5
# n = 4
# a = []
# #for i in range(N):
#  #   for j in range(M-1):
#  #       a[[i][j]] = int(input())
# #        a[i,j] = input("Введите число позиции i = ", i , " , j = ", j)
# #        print(a[i][j], end='')
#
# for i in range(0,m-1):
#     for j in range(0,n-1):
#         a = 5
#     print(a)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.