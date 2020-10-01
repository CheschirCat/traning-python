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






