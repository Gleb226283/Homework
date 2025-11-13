from datetime import datetime

months = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }

while True:
    text = input("Введите дату или end: ")
    if text == 'end':
        break
    try:
        date_list = text.split(',')
        parts = [item.strip() for item in date_list]
        if len(parts) == 3:
            week, month_day, year = parts  # исправил month на month_day
            month_name, day = month_day.split()  # теперь month_day определен
            month_num = months[month_name]  # исправил month на month_num
            print(datetime(int(year), month_num, int(day)))
        elif len(parts) == 2:
            week, date_part = parts
            if '.' in date_part:
                day, month, year = date_part.split('.')
                year = "20" + year
                print(datetime(int(year), int(month), int(day)))
            else:
                day, month_name, year = date_part.split()
                print(datetime(int(year), months[month_name], int(day)))
        else:
            print("Неверный формат!")
    except Exception as e:
        print("Ошибка! Попробуйте снова.")