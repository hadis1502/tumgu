documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

def p(documnet_number):
    for x in documents:
        if x['number'] == documnet_number:
            return ("Владелец документа: " + x['name'])
    return "Владелец документа: владелец не найден"
        
def s(document_number):
    for k in directories:
        if document_number in directories[k]:
            return ("Документ хранится на полке:" + k)
    return "Документ хранится на полке: документ не найден"
def l():
    command = input("Введите номер команды (p, s): ")
    if command == 'p':
        document_number = input("Введите номер: ")
        print(p(document_number))
    elif command == 's':
        document_number = input("Введите номер: ")
        print(s(document_number))
    else: print("Команда не найдена")
        
l()