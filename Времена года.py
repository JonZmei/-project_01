month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month_names = {
    'январь': 1,
    'февраль': 2,
    'март': 3,
    'апрель': 4,
    'май': 5,
    'июнь': 6,
    'июль': 7,
    'август': 8,
    'сентябрь': 9,
    'октябрь': 10,
    'ноябрь': 11,
    'декабрь': 12
}

month_input = input("Введите номер месяца или название месяца на русском языке: ")
if month_input.isdigit():
    month_number = int(month_input)
    if month_number in month_days:
        days = month_days[month_number]
        month_name = {
            1: 'январь',
            2: 'февраль',
            3: 'март',
            4: 'апрель',
            5: 'май',
            6: 'июнь',
            7: 'июль',
            8: 'август',
            9: 'сентябрь',
            10: 'октябрь',
            11: 'ноябрь',
            12: 'декабрь'
        }[month_number]
        print(f"Вы ввели {month_name}. {days} дней")
    else:
        print("Такого месяца нет!")
elif month_input in month_names:
    month_number = month_names[month_input]
    days = month_days[month_number]
    print(f"Вы ввели {month_input}. {days} дней")
else:
    print("Неверный формат ввода!")
