#TODO строки

'asdfghjklqwerty'

"asdfghjqwerty"

'''asdfgh
jklqwe
rtyu'''

\n #перенос строки

#TODO олперации со строками
#умножение
In [30]: 'hello' * 3
Out[30]: 'hellohellohello'
#сложение
In [31]: 'hello ' + 'world'
Out[31]: 'hello world'
# сравнение
In [32]: 'hello' == 'hello'
Out[32]: True
In [33]: 'hello' == 'hello1'
Out[33]: False
In [34]: 'hello' > 'hello'
Out[34]: False

# кодирование декодирование
'привет'.encode()
In [35]: 'привет'.encode()
Out[35]: b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'

b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode()
In [36]: b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode()
Out[36]: 'привет'

b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode('utf8')
In [37]: b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode('utf8')
Out[37]: 'привет'

b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode('cp1251')
In [38]: b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode('cp1251')
Out[38]: 'РїСЂРёРІРµС‚'


#TODO индексация строк
'qwerty'[0]   запрос значения из строки 0->первый символ
In [44]: 'qwerty'[0]
Out[44]: 'q'

'qwerty'[1]   1->первый символ
In [45]: 'qwerty'[1]
Out[45]: 'w'

'qwerty'[-1]   -1->последний  символ
In [46]: 'qwerty'[-1]
Out[46]: 'y'

'qwerty'[2:4]  диапазон со 2 символа по 4, четвертый не входит
In [47]: 'qwerty'[2:4]
Out[47]: 'er'
'qwerty'[2:-1]
In [48]: 'qwerty'[2:-1]  с 2 по 3
Out[48]: 'ert'
'qwerty'[:4]
In [49]: 'qwerty'[:4] с 1 по 4, четвертый не входит
Out[49]: 'qwer'
'qwerty'[4:] с 4 и до конца
In [50]: 'qwerty'[4:]
Out[50]: 'ty'
'qwerty'[:4] + 'qwerty'[4:]
In [51]: 'qwerty'[:4] + 'qwerty'[4:]
Out[51]: 'qwerty'
'qwerty'[:]
In [52]:  'qwerty'[:]
Out[52]: 'qwerty'

# шаг
'qwertyuiopasdfghjklzxcvbnm'[:20:2] с первого символа по двадцатый отбирает каждый второй
In [53]: 'qwertyuiopasdfghjklzxcvbnm'[:20:2] # каждый 2
Out[53]: 'qetuoadgjl'
'qwertyuiopasdfghjklzxcvbnm'[:20:3]
In [54]: 'qwertyuiopasdfghjklzxcvbnm'[:20:3] # каждый 3
Out[54]: 'qrupdhl'
'qwertyuiopasdfghjklzxcvbnm'[-20:0:-3]
In [60]: 'qwertyuiopasdfghjklzxcvbnm'[-20:0:-3]
Out[60]: 'ur'
'qwertyuiopasdfghjklzxcvbnm'[-25:0:-3]
In [62]: 'qwertyuiopasdfghjklzxcvbnm'[-25:0:-3]
Out[62]: 'w'
'qwertyuiopasdfghjklzxcvbnm'[::-1]   # можно развернуть строку
In [63]: 'qwertyuiopasdfghjklzxcvbnm'[::-1]
Out[63]: 'mnbvcxzlkjhgfdsapoiuytrewq'

In [64]: len('qwertyuiopasdfghjklzxcvbnm') # длинна строки
Out[64]: 26

# TODO методы у строк
rav = 'Toyota RAW4'
rav = 'Toyota RAW4'
rav.find('a') # поиск символа в строке
Out[4]: 5 # -> номер символа с начала строки
rav.rfind('y') # -> номер символа с конца строки
Out[6]: 2
rav.replace('a', 'b') # замена сивола в строке
Out[7]: 'Toyotb RAW4'
rav.upper() # все к верхнему регистру
Out[8]: 'TOYOTA RAW4'
rav.lower() # все к нижнему регистру
Out[9]: 'toyota raw4'
rav.title() # заглавные
Out[10]: 'Toyota Raw4'
rav.isalpha() # проверка все ли символы являютс буквами
Out[11]: False
rav.isalnum() # проверка все ли символы являютс цифрами
Out[12]: False

coordin = '100'
print(coordin.isalnum())
print()
print(type(coordin))
print()
c = int(coordin) # конвертация str в int
print(type(c))
print(c)
print()
x = float(coordin) # конвертация int в float
print(type(x))
print(x)
print()
q = str(coordin) # конвертация float в str
print(type(q))
print(q)






