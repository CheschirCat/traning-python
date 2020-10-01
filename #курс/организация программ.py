# вывод данных
print(2 ** 10)
print('два в степени десять', 2 ** 10)
# 1024
# два в степени десять 1024

# ввод данных
user_input = input('Введите координаты: ')
print(type(user_input))
print(user_input)
print()

x, y = map(int, input().split()) # конвертация типа строки из str в int
print(type(x))
print(x, y)


