my_list = [] #  пустой список
my_list = [1, 2, 3, 4, 5]
print(my_list)

my_list.append('qweqwe')
print(my_list)

# срез списка
print(my_list[-2])
print(my_list[:-3])
print(my_list[-2: ])
print(my_list[::2])

# добавлени к списку
my_list.append(77)
print(my_list)

# расширение списка
my_list.extend([5, 5, 5, ])
print(my_list)
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
print(zoo)
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ('rooster', 'ostrich', 'lark')
zoo.extend(birds)
print(zoo)

# выведите на консоль индкса элемента
print('лев сидит в клетке ', zoo.index('lion') + 1)
print('жаворонок сидит в клетке ', zoo.index('lark') + 1)


# добавление в конкретное место
my_list.insert(3, 'aaa')
print(my_list)

# получение объекта из списка
print(my_list[5])

# удаление объекта из списка
del my_list[6]
print(my_list)

# удаление объекта по значению из списка
my_list.remove(5)
print(my_list)

# сложение списка
print(my_list+ [6, 7, 8])

# умножение списка
print(my_list * 3)
print(my_list)

# список списков
matrix =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

print(matrix[1]) # срез элементов
print(matrix[1][1])

# сравнение списков
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] == [3, 2, 1])
print([1, 2, 3] > [3, 2, 1])
print([1, 2, 3] < [3, 2, 1])

# входит ли объект в список
print(my_list)
print(5 in my_list)
print(7 in my_list)
print(id (my_list))

# генератор чисел range
list(range(10))
#Out[46]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(range(5, 10)) # с интервалом от 5 до 10
#Out[50]: [5, 6, 7, 8, 9]

list(range(5, 10, 3)) # с интервалом и шагом 3 от 5 до 10
#Out[51]: [5, 8]

# методы списка то же что  и у строки
my_list
#Out[53]: [1, 2, 3, 4, 5, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
my_list.count(5) # кло-во 5 в списке
#Out[52]: 1
my_list.extend([5, 6, 5, 5])

# min  max в  списке,  минимальное или максимальное число в списке
del my_list[3]
min(my_list)
#Out[62]: 1
#Out[63]: [1, 2, 3, 4, 5, 5, 6, 5, 5]
max(my_list)
#Out[64]: 6

# сортировка
my_list.insert(1, 444)
my_list
#Out[67]: [1, 444, 2, 3, 4, 5, 5, 6, 5, 5]
my_list.sort()
my_list
#ut[69]: [1, 2, 3, 4, 5, 5, 5, 5, 6, 444]

# изменяемые и не изменяемые списки изменяемые, строки нет
my_list
#Out[69]: [1, 2, 3, 4, 5, 5, 5, 5, 6, 444]
second_list = my_list
my_list.append(100)
my_list
#Out[72]: [1, 2, 3, 4, 5, 5, 5, 5, 6, 444, 100]
second_list
#Out[73]: [1, 2, 3, 4, 5, 5, 5, 5, 6, 444, 100]

raw4 = '123456789'
raw4.append() # строки не изменяемые

my_list[1] = 300
my_list
Out[82]: [1, 300, 3, 4, 5, 5, 5, 5, 6, 444, 100]

raw4.replace('1', '3') # можно создать новую строку, но старая остается той же
Out[83]: '323456789'
raw4
Out[84]: '123456789'

my_list[-1] = 222
Out[85]: [1, 300, 3, 4, 5, 5, 5, 5, 6, 444, 222]


valve = 42
id(valve)
Out[94]: 1954785856
mass = valve
id(mass)
Out[95]: 1954785856

mass = mass + 1
id(mass)
Out[96]: 1954785872

mass = mass - 1
id(mass)
Out[97]: 1954785856

valve = 42
id(valve)
Out[94]: 1954785856
mass = valve
id(mass)
Out[95]: 1954785856

mass = mass + 1
id(mass)
Out[96]: 1954785872

mass = mass - 1
id(mass)
Out[97]: 1954785856


raw4 = 'toyota'
id(raw4)
Out[98]: 96352864

my_car = raw4
id(my_car)
Out[100]: 96352864
my_car + 'raw4'
id(my_car)
Out[103]: 96352864
my_car = my_car + 'raw4'
id(my_car)
Out[104]: 95185480
my_car
Out[105]: 'toyotaraw4'
raw4
Out[106]: 'toyota'
#  числа и строки не изменяемые

# умножение списков с сюрпризом
[[], []] * 3
Out[86]: [[], [], [], [], [], []]

many_list = [[], []] * 5
Out[90]: [[], [], [], [], [], [], [], [], [], []]
many_list[1] = 300
Out[91]: [[], 300, [], [], [], [], [], [], [], []]
many_list[0].append(42)
Out[93]: [[42], 300, [42], [], [42], [], [42], [], [42], []]













