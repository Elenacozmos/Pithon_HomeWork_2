def zadacha1():

# # Задача 1. Напишите программу, которая принимает на вход число N
# # и выдает список факториалов для чисел от 1 до N.
# # пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

    num = int(input('введите число: '))
    sumi = 1
    for i in range(1, num+1):
        sumi = sumi*i
        print(sumi, end=' , ')
zadacha1()


def zadacha2():
# # Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
# # x = [0, 1]
# # y = [0, 1]
# # z = [0, 1]

	for x in range(0, 2):
			for y in range(0, 2):
					for z in range(0, 2):
							result = not (x and y) or z
							print(f'{x}, {y}, {z}, {int(result)}')
zadacha2()


def zadacha3():
# # Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки 
# встречается во второй
# # «one» «onetwonine» - o – 2, n – 3, e – 2

	string_1 = 'one'
	string_2 = 'onetwonine'
	for i in range(len(string_1)):
			count = 0
			for j in range(len(string_2)):
					if string_1[i] == string_2[j]:
							count += 1
			print(f'{string_1[i]} - {count} раз(а)')
zadacha3()


def zadacha4():
    # Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
    # Сдвиньте все элементы списка на 2 позиции вправо.
    # 3 -> [2, 3, -3, -2, -1, 0, 1]

    n = int(input('введите N: '))
    shift = int(input('на сколько позиций сместить вправо: '))
    list = []

    for i in range(-n, n + 1):
        list.append(i)

    print(list[-shift:] + list[:-shift])


zadacha4()
