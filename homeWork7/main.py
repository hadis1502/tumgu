import csv
import os

def load_csv_data(filename):
    """Загружает данные из CSV-файла."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл не найден: {filename}")
    
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
       # print(list(reader))
        return list(reader)

def parse_client_data(raw_data):
    """Парсит и извлекает атрибуты ."""
    return {
        'full_name': raw_data['name'],
        'gender': raw_data['sex'],
        'age': int(raw_data['age']),
        'device': raw_data['device_type'],
        'browser': raw_data['browser'],
        'amount': int(raw_data['bill']),
        'region': raw_data['region']
    }

def format_gender(gender):
    """Форматирует пол в читаемую форму."""
    gender_map = {'male': 'мужского пола', 'female': 'женского пола'}
    return gender_map.get(gender, 'неизвестен')

def format_device(device):
    """Форматирует название устройства."""
    device_map = {
        'mobile': 'мобильного',
        'desktop': 'стационарного компьютерного',
        'laptop': 'портативного компьютерного',
        'tablet': 'планшетного'
    }
    return device_map.get(device, device)

def generate_client_description(client_data):
    """Генерирует текстовое описание  по шаблону."""
    formatted_gender = format_gender(client_data['gender'])
    formatted_device = format_device(client_data['device'])
    
    # Согласование глагола с полом
    verb = 'совершила' if client_data['gender'] == 'female' else 'совершил'
    
    description = (
        f"Пользователь {client_data['full_name']} {formatted_gender}, "
        f"{client_data['age']} лет {verb} покупку на {client_data['amount']} у.е. "
        f"с {formatted_device} браузера {client_data['browser']}. "
        f"Регион, из которого совершалась покупка: {client_data['region']}."
    )
    
    return description

def process_clients(input_filename, output_filename):
    """Основная функция для обработки данных и записи в файл."""
    # 1: Загрузка данных
    raw_clients = load_csv_data(input_filename)
    
    # 2–3: Парсинг и преобразование данных
    parsed_clients = [parse_client_data(client) for client in raw_clients]
    
    # 4: Формирование описаний
    descriptions = [generate_client_description(client) for client in parsed_clients]
    
    # 5: Запись в файл
    with open(output_filename, 'w', encoding='utf-8') as file:
        for description in descriptions:
            file.write(description + '\n')

if __name__ == '__main__':
    try:
        process_clients('web_clients_correct.csv', 'client_descriptions.txt')
        print("Обработка завершена успешно!")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
