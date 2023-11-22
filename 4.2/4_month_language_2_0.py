def month(month_number, language="ru"):
    months_ru = {
        1: 'Январь',
        2: 'Февраль',
        3: 'Март',
        4: 'Апрель',
        5: 'Май',
        6: 'Июнь',
        7: 'Июль',
        8: 'Август',
        9: 'Сентябрь',
        10: 'Октябрь',
        11: 'Ноябрь',
        12: 'Декабрь'
    }

    months_en = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    if language == 'ru':
        return months_ru.get(month_number, 'Неверный номер месяца')
    elif language == 'en':
        return months_en.get(month_number, 'Invalid month number')
    else:
        return 'Неподдерживаемый язык'


print(month(7))
