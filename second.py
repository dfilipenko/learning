first_list = ['word', 10, 6.0, 'new word'] #First exercise
print (type(first_list))
print (type(first_list[0]), type(first_list[1]), type(first_list[2]), type(first_list[3]))
second_list = list(input('Введите элементы списка')) #Second exercise
print(second_list)
new_list = []
k = 0
for i in range(int(len(second_list) / 2)):
    second_list[k], second_list[k + 1] = second_list[k + 1], second_list[k]
    k += 2
    new_list = second_list
print(new_list)
season = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] #Third exercise
a = int(input('Введите число от 1 до 12: '))
m = season.index(a)
if m < 3:
    print ('Зима')
if 2 < m < 6:
    print('Весна')
if 5 < m < 9:
    print ('Лето')
if 8 < m <= 12:
    print('Осень')
season = {1 : "winter", 2 : "winter", 3 :  "spring", 4 : "spring", 5 : "spring", 6 : "summer", 7 : "summer", 8 : "summer", 9 : "autumn", 10 : "autumn", 11 : "autumn", 12 : "winter"}
a = int(input('Введите число от 1 до 12: '))
print(season.get(a))
my_str = input('Введите несколько слов, разделенных пробелом: ') #Fourth exercise
new_str = my_str.split(' ')
for index, value in enumerate(new_str):
    print(index+1, value[:10])
my_list = [2, 4, 7, 9, 12, 16] #First exercise
a = int(input('Введите целое число: '))
my_list.append(a)
my_list.sort(reverse=True)
print(my_list)
set_prod = list() #Sixth exercise
while True:
    name = input('Введите название: ')
    price = input ('Введите цену: ')
    quantity = input('Введите количество: ')
    unit = input('Введите единицу измерения: ')
    next = input('Хотите ввести следующий товар? (да/нет)')
    product = {"название": name, "цена": price, "количество": quantity, "ед.": unit}
    set_prod.append(product)
    if next.lower() == "нет":
        break
for index, value in enumerate(set_prod):
    print(index+1,value)
list_name = list()
list_price = list()
list_guatity = list()
list_unit = list()
for item in set_prod:
    name = item.get("название")
    list_name.append(name)
    price = item.get("цена")
    list_price.append(price)
    qantity = item.get("количество")
    list_guatity.append(quantity)
    unit = item.get("ед.")
    list_unit.append(unit)
analitic = {"Название" : list_name, "Цена" : list_price, "Количество" : list_guatity, "Единицы" : list_unit}
print(analitic)





