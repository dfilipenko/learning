def division (a, b): #First exercise
    try:
        c = a / b
    except ZeroDivisionError:
        return
    return c
n = division (int(input('Введите число а: ')), int(input('Введите число b: ')))
print (n)
def anketa (name, surname,year, city, email, phone):            #Second exercise
    print (f"Имя - {name}, Фамилия - {surname}, Год рождения - {year}, Город - {city}, E-mail - {email}, Телефон - {phone}")

n = anketa(name = input('Введите имя:  '), surname = input('Введите фамилию: '), year = int(input('Введите год рождения')), city = input('Введите город проживания: '), email = input('Введите город e-mail: '), phone = input('Введите гномер телефона: '))
print(n)
def my_func (a, b, c):      #Third exercise
    d = min (a, b, c)
    n = a + b + c - d
    return n
m = my_func(int(input('Введите а: ')), int(input('Введите b: ')), int(input('Введите c: ')))
print(m)

x = abs(float(input('Введите число х: ')))          #Fourth exercise
y = int(input('Введите целое отрицательное число y: '))
from functools import reduce
def my_func (x, y):
    step = []
    for c in range(abs(y)):
        step.append(x)
    result_func = 1 / reduce((lambda k, m: k * m), step)
    return result_func
print (my_func(x, y))
stop = input('Введите стоп-символ: ')             #First exercice
my_str = input('Введите строку из чисел, разделенных пробелом: ').split()
while my_str.count(stop) == 0:
    int_str = map(int, my_str)
    result_sum = sum(int_str)
    print (result_sum)
    my_str_plus = input('Введите строку из чисел, разделенных пробелом: ').split()
    if my_str_plus.count(stop) > 0:
        index = my_str_plus.index(stop)
        fin_str = my_str_plus[:index]
        my_str.extend(fin_str)
        int_str = map(int, my_str)
        result_sum = sum(int_str)
        print(result_sum)
        break
    else:
        my_str.extend(my_str_plus)
        continue

def int_func(text):         #Sixth exercise
    return text.title()

input_text = input('Введите текст маленькими буквами: ').split()
final = list(map(int_func, input_text))
res_txt = ' '.join(final)
print(res_txt)