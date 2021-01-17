class Date:                           #First exercise

    def __init__(self, date):
        self.date = date

    @classmethod
    def int_date(cls, date):
        date_list = date.split('-')
        date_list = list(map(int, date_list))
        return date_list

    @staticmethod
    def valid_date(date_list):
        if date_list[0] > 31 or date_list[0] < 1:
            print ('Некорректное число')
        if date_list[1] > 12 or date_list[1] < 1:
            print ('Некорректный месяц')
        if len(str(date_list[2])) != 4:
            print('Некорректный год')
        else:
            print('Дата введена корректно')
        return ''

print(Date.int_date('3-11-2020'))
print(Date.valid_date([3, 11, 2020]))

class DevisionError(Exception):              #Second exercise
    def __init__(self, text):
        self.text = text

a = int(input('Введите числитель: '))
b = int(input('Введите знаменатель: '))

while True:
    if b == 0:
        err = DevisionError('Делить на ноль нельзя!')
        print(err)
        b = int(input('Введите знаменатель: '))
        continue
    else:
        print (a / b)
        break

class Error(Exception):                          #Third exercise

    def __str__(self):
        return 'Введенный элемент не является числом'

class NumberList:

    number_list = []
    @classmethod
    def add_number(cls):
        while True:
            number = input('Введите число(для завершения наберите stop): ')
            try:
               cls.number_list.append(int(number))
            except ValueError as err:
                err = Error()
                if number == 'stop':
                    print(cls.number_list)
                    break
                else:
                    print(err)
                    continue
        return ''

print(NumberList.add_number())

class Warehouse:                                               #Fourth, fifth, sixth exercise

    @staticmethod
    def product_in_stock(*kwargs):
        stock_list = []
        division_list = []
        for goods in kwargs:
            stock_ask = input(f'Принять товар {goods} на склад или в подразделение? S - склад, D - подразделение ')
            if stock_ask == 'S' or stock_ask == 's':
                stock_list.append(goods)
                print(f"Товар {goods} добавлен на склад")
            elif stock_ask == 'D' or stock_ask == 'd':
                division_list.append(goods)
                print(f"Товар {goods} отправлен в подразделение")
            else:
                print('Введен некорректный ответ')
        return f"Товары на складе: {stock_list}\nТовары в подразделениях: {division_list}"

class Equipment:

    def __init__(self, brand, number, price):
        self.brand = brand
        self.number = number
        self.price = price
        self.item = {
            'brand': self.brand,
            'number': self.number,
            'price': self.price,
        }

    def __str__(self):
        return str(self.item)

class Notebook(Equipment):

    def __init__(self, brand, number, price, OS):
        super().__init__(brand, number, price)
        self.OS = OS
        self.item['OS'] = self.OS

class Printer (Equipment):

    def __init__(self, brand, number, price, color):
        super().__init__(brand, number, price)
        self.color = color
        self.item['color'] = self.color

class Scaner (Equipment):

    def __init__(self, brand, number, price, scan_type):
        super().__init__(brand, number, price)
        self.scan_type = scan_type
        self.item['scan_type'] = self.scan_type



note_1 = Notebook('hp', 2367, 10256, 'Windows')
note_2 = Notebook ('Sumsung', 1547, 48750, 'Linux')
print_1 = Printer('Xerox', 6641, 6214, 'color')
scan_1 = Scaner('HP', 2176, 3500, 'upper')
print(note_1)
print(note_2)
print(print_1)
print(scan_1)

print(Warehouse.product_in_stock(note_1.item, note_2.item, print_1.item, scan_1.item))

class Complex:                              #Seventh exercise

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"Сумма двух чисел равна ({self.a + self.b} + {other.a + other.b}) * i"

    def __mul__(self, other):
        return f"Произведение двух чисел равно ({(self.a * other.a) - (self.b * other.b)} + {(self.b * other.a) + (self.a * other.b)}) * i"

first = Complex (1, 5)
second = Complex (4, 11)
print(first + second)
print(first * second)
