import json
import csv

def process_visits_optimized():
    # Создаем временный файл с mapping user_id -> category
    with open('purchase_log.txt', 'r', encoding='utf-8') as purchase_file, \
         open('temp_mapping.csv', 'w', newline='', encoding='utf-8') as temp_file:
        
        temp_writer = csv.writer(temp_file)
        
        for line in purchase_file:
            try:
                purchase_data = json.loads(line.strip())
                user_id = purchase_data.get('user_id')
                category = purchase_data.get('category')
                
                if user_id and category:
                    temp_writer.writerow([user_id, category])
            except json.JSONDecodeError:
                continue
    
    # Загружаем mapping в память (предполагаем, что он помещается)
    purchase_dict = {}
    with open('temp_mapping.csv', 'r', encoding='utf-8') as temp_file:
        reader = csv.reader(temp_file)
        for row in reader:
            if len(row) >= 2:
                purchase_dict[row[0]] = row[1]
    
    # Обрабатываем visit_log.csv
    with open('visit_log__1_.csv', 'r', encoding='utf-8') as visit_file, \
         open('funnel.csv', 'w', newline='', encoding='utf-8') as funnel_file:
        
        reader = csv.reader(visit_file)
        writer = csv.writer(funnel_file)
        
        writer.writerow(['user_id', 'source', 'category'])
        next(reader, None)  # Пропускаем заголовок
        
        for row in reader:
            if len(row) >= 2 and row[0] in purchase_dict:
                writer.writerow([row[0], row[1], purchase_dict[row[0]]])
    
    # Удаляем временный файл
    import os
    os.remove('temp_mapping.csv')

if __name__ == "__main__":
    process_visits_optimized()