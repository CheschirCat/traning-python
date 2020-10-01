#TODO переменные
#TODO действия с переменными
car = 'Toyota raw4'
#In [3]: print(car)
#Toyota raw4

In [4]: len(car) #длинна знаения переменной
Out[4]: 11

In [5]: car[-4]  #вывод знаения по индексу
Out[5]: 'r'

In [6]: car[::-1] #вывод знаения по индексу
Out[6]: '4war atoyoT'
#TODO присвоение нескольким переменным одного и того же значения
car = 'Toyota raw4'
my_favorite = car #несколько переменных могут иметь одно и тоже значение
print(my_favorite)
Toyota raw4
print(car)
Toyota raw4

#TODO множественное присвоение значения
x = y = z = 0
print(x)
print(y)
print(z)
0
0
0

car = my_favorite = rav = 'Toyota RAW4'
print(car)
print(my_favorite)
print(rav)
Toyota RAW4
Toyota RAW4
Toyota RAW4
# TODO множественная иницилизация
my_car, may_wife = 'Toyota RAW4', 'Лена'
print(my_car)
print(may_wife)
Toyota RAW4
Лена

x, y, z = car, 151, 2
print(x)
print(y)
print(z)
Toyota RAW4
151
2

# TODO динамицеская типизация
my_car = 'RAV4'   # присваивание значения
print(type(my_car)) # выводит какого типа данные находятся в переменной
print(my_car)
my_car = 42        # изменение присвоенного значения
print(type(my_car)) # выводит какого типа данные находятся в переменной
print(my_car)
<class 'str'>
RAV4
<class 'int'>
42

# TODO какого типа данные находятся в переменной
print(type(my_car)) # выводит какого типа данные находятся в переменной
<class 'int'>
print(isinstance(x, int))# определяет какого типа данные находятся в переменной
False
print(isinstance(x, str))
True
# TODO проверить одинаковое значение у разных переменных
print(id(x))  # id перенменной
89794544
t = x
print(id(t))
89794544
89794544


