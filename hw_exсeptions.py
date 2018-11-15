formula_string = list(input('Введите выражение (оператор(+ - * /) число1 число2):').split())


def polish_notation(formula_string):
    try:
        assert float(formula_string[1]) >= 0 and float(formula_string[2]) >= 0, 'Введите положительное число'
        if formula_string[0] == '+':
            print(float(formula_string[1]) + float(formula_string[2]))
        elif formula_string[0] == '-':
            print(float(formula_string[1]) - float(formula_string[2]))
        elif formula_string[0] == '*':
            print(float(formula_string[1]) * float(formula_string[2]))
        elif formula_string[0] == '/':
            try:
                answ = 0
                answ = float(formula_string[1]) / float(formula_string[2])
                print(answ)
            except ZeroDivisionError:
                print('На ноль не делим')
        else:
            print('Введен недоступный оператор')
    except IndexError:
        print('Недостаточно данных')


polish_notation(formula_string)
