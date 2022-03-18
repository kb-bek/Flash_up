# Задание №1:

# Если взять ВСЕ числа от 0 до 10, которые деляться на 3 или 5 БЕЗ ОСТАТКА, то получим 3, 5, 6 и 9.
# Сумма этих чисел равна 23 (3+5+6+9) = 23.

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

sum = 0
n = 1000
a = [list(range (1 , 1000))]
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        print(sum)

#Задание №2:
# Поменяйте значения переменных местами(НЕ ВРУЧНУЮ!),
# чтобы в ПЕРЕМЕННОЙ "a" было значение 555, а в ПЕРМЕННОЙ "b" было значение 333.
a = 333
b = 555
c = a
a = b
b = c
print(a,b)



# Задание №3:
# Если взять строку - "237" и сложить все её числа то получится 2+3+7 = 12.
# Возьмите строку "4729461084" и сложите все её числа.
# Результат выведите на экран.

a = 4+7+2+9+4+6+1+0+8+4
print(a)


# Задание 4:
# Создайте input() который принимает от пользователя дату в формате: "2020-10-24 18:30"
# и возвращает dictionary разделённую по значениям даты:


date = {"2020-10-24 18:30" 
        "year": "2020",
        "month": "10",
        "day": "24",
        "time": "18:30"}

print(type (date))
a = input('введите дату:')

if a == "2020-10-24 18:30":
    print(date)


# Задание №5:
# Какое слово нужно сложить 5 раз чтобы получить число 5?
# Какое слово нужно умножить на 7 чтобы получить 7?
a = True
b = a + a + a + a + a
print(b)
a1 = True
b1 = a1 * 7
print(b1)


# Задание №6:
# Напишите команду Linux которая создаст ДИРЕКТОРИЮ в НЕСУЩЕСТВУЮЩЕЙ директории БЕЗ ОШИБОК!

#ls

#cd

#mkdir < name dic>

# Задание №7:
# Как в Linux выглядит полный путь до Desktop Директории для пользователя 'developer'.
# /home/developer/desktop/.

# Задача 1
# Есть список:
# Выведите все элементы, которые больше 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a :
    if i > 5:
         print(i)

#Задача 2
# Есть набор чисел
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# Поделить каждое число из digits на 9 и вывести на экран.

digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
a = list(digits)
for i in digits:
    a1 = i / 9
    print(a1)




# Задача 3
# Здесь замешаны разные типы данных.
# Напишите программу, которая берёт массив данных spisok2 и выводит только те элементы из spisok_2, которых нет в spisok_1.
# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)


spisok_1 = ['Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23]
spisok_2 = ['Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23]

spisok_3 = [x for x in spisok_2 if x not in spisok_1]
print(spisok_3)

#Задание 1:
# Напишите программу, которая выводит чётные числа из списка длиною 300 объектов
#    и останавливается, если встречает число 23

for i in range(2, 300, 2):
    if i == 238:
        break
    print(i)

# Задание 2:
# 1. Спросите у пользователя предложение и поделите его по пробелам.
    # Если пользователь ввёл меньше шести слов спросите снова, Не принимайте предложения если оно корочволов, спрашивайте снова и снова.
# 2. Поделите полученный лист на 2 равные части (Если число элементов листа нечетное, то длина первой части должна быть на один жлемент больше)
# 3. Переставьте эти две части местами и запишите в лист.

while True:
    a = input("Напишите предложение: ")
    a = a.split()
    if len(a) > 6:
        break
print(a)

first_part = []
second_part = []
if len(a) % 2 != 0:
    first_part = a[0 : int(len(a) / 2) + 1]
    second_part = a[int(len(a) / 2) + 1 : len(a)]
else:
    first_part = a[0: int(len(a) / 2)]
    second_part = a[int(len(a) / 2) : len(a)]
print(first_part)
print(second_part)

list = first_part + second_part
print(list)


# Задание 3:
# Вам дан список:
# Определите количество четных и не четных.
numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
print([x for x in [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9] if x % 2 == 0])
print([x for x in [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9] if x % 2 != 0])

# Задание 4:
# Дан список  целых чисел:
# numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# Создайте новый лист и замените отрицательные числа на -1, положительные на число 1, ноль оставить без изменения.


numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
a = []
for i in range(len(numbers)):
    if numbers[i]>0:
        a.append(1)
    elif numbers[i]<0:
        a.append(-1)
    else:
        a.append(0)
print(a)


# Задание 5:
# Выведите все элементы списка с четными ИНДЕКСАМИ (то есть A[0], A[2], A[4], ... ])
my_list = [2,4,6,8,10,1,3,5,7,9,11,13,17]
for el in range(0,len(my_list)):
    if el % 2 == 0:
        print(el)
    else:
        pass

#Задание 6
#     Дано четырехзначное число. Верно ли, что цифры в нем расположены по убыванию?
#     Например, 4311 - нет, 4321 - да, 5542 - нет, 5631 - нет, 9871 - да.
a = list (input('Введите число:'))
if a [0]> a [1] and a[1] > a[2] and a[2] > a[3] :
    print('yes')
else:
    print('no')


