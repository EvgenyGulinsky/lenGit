def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i)
    for i in range(base // 2, 0, -1):
        print(fill * i)
    pass


def print_fio(name, surname, patronymic):
    print('Инициалы - ', surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')
    pass


def print_digit_sum(num):
    summ = 0
    while num > 0:
        summ += num % 10
        num //= 10
    print('сумма цифр числа =', summ)
    pass

"""коммент"""

while True:
    print("Введите:")
    print('1. Отрисовка треугольника')
    print('2. Для вывода инициалов')
    print('3. Для вычисления суммы цыфр числа')
    print('0. Выход')

    match input('>> '):
        case '1':
            draw_triangle(input('Введите чем заполнять треугольник >> '),
                          int(input('Введите предельную высоту треугольника >> ')))
        case '2':
            print_fio(input('Введите имя >> '), input('Введите Фамилию >> '), input('Введите Отчество >> '))
        case '3':
            print_digit_sum(int(input('Введите цело число произвольной длинны')))
        case '0':
            exit(0)
        case _:
            print('Неверный ввод!')