from datetime import datetime

MOSCOW_TIMES = 'The Moscow Times'
GUARDIAN = 'The Guardian'
DAILY_NEWS = 'Daily News'

def get_moscow_times_time(val):
    return datetime.strptime(val, '%A, %B %d, %Y')

def get_guardian_time(val):
    return datetime.strptime(val, '%A, %d.%m.%y')

def get_daily_news_time(val):
    return datetime.strptime(val, '%A, %d %B %Y')

formatters_map = {
    MOSCOW_TIMES: get_moscow_times_time,
    GUARDIAN: get_guardian_time,
    DAILY_NEWS: get_daily_news_time
}

def get_time_by_publisher(publisher_name, d):

    try:
        current_fn = formatters_map[publisher_name]
        if current_fn:
          return current_fn(d)
        
    except:
        print('Wrong datetime format')
        return ''

while True:
    user_input = input("Введите название и дату выпуска газеты через дефис (или специальный символ q для выхода): ")
    
    if user_input == "q": 
        break

    user_input_arr = user_input.split(' — ', maxsplit=2)

    if len(user_input_arr) == 2:
        res = get_time_by_publisher(*user_input_arr)
        
        if res:
            print(res)
