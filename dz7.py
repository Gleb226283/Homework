def load_clients(filename):
    """Загружает данные клиентов из CSV файла"""
    clients = []
    with open('web_clients_correct-staroe.csv', 'r') as file:
        with open('File.7.txt', 'w') as file7:
            headers = file.readline().strip().split(',')
            for line in file:
                line = line.strip()
                parts = line.split(',')
                name = parts[0]
                device = parts[1]
                browser = parts[2]
                sex = parts[3]
                age = parts[4]
                bill = parts[5]
                region = parts[6]
                if sex == 'female':
                    gender = 'женского'
                    verb = 'совершила'
                else:  # male
                    gender = 'мужского'
                    verb = 'совершил'

                    # Переводим устройство
                device_translation = {
                    'mobile': 'мобильного браузера',
                    'tablet': 'браузера планшета',
                    'laptop': 'браузера ноутбука',
                    'desktop': 'браузера компьютера'
                }
                device_ru = device_translation.get(device, device)

                # Формируем описание
                description = (
                    f"Пользователь {name} {gender} пола, "
                    f"{age} лет {verb} покупку на "
                    f"{bill} у.е. с {device_ru} "
                    f"{browser}. "
                    f"Регион, из которого совершалась покупка: {region}.\n\n"
                )
                file7.write(description)
    return clients

