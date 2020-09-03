from datetime import datetime
import json
from definitions import LOG_PATH


#Написать декоратор из п.1, но с параметром – путь к логам.

path = input(f'Пожалуйста, введите путь к логам (при пустом вводе используем {LOG_PATH}\log_path.json): ')
path = path or LOG_PATH
print('Сохраняем логи в папке: ', path)

###def pathed_decor_logger(path):

def decor_logger(path):
    LOGFILE = f'{path}\log_path.json'
    print(LOGFILE)
    log_entry = None

    with open(LOGFILE, 'w', encoding='utf-8') as f:
        json.dump([], f)

    def _decor_logger(old_function):

        def new_function(*args, **kwargs):
            date = str(datetime.now().date())
            time = str(datetime.now().time())
            old_result = old_function('abc000', 'erd000')
            log_entry = f'Date: {date}, Time: {time}, Function name: {old_function.__name__}, Args: {str(args)}, Kwargs: {str(kwargs)}, Result: {old_result};'
            #print('***', type(log_entry))'
            #print('***', type(log_entry))
            print('В лог будет сохранена следующая запись: ', log_entry)
            # сохранение результата в файл
            with open(LOGFILE, 'a', encoding='utf-8') as f:
                json.dump(log_entry, f, ensure_ascii=False, indent=4)
                f.write('\n')
            print('Лог-запись успешно добавлена в локальный файл:', LOGFILE)
            #print('***', new_function.__name__)
            return old_result

        return new_function

    return _decor_logger
    #return new_function.__name__
#return decor_logger

@decor_logger(LOG_PATH)
def concat(str_1, str_2):
    return print(f'{str_1}{str_2}')
print(concat('abc', 'erd'), '\n')
print(concat('abc', 'erd1'), '\n')
print(concat('abc', 'erd2'), '\n')
print(concat('abc', 'erd3'), '\n')
print(concat('abc', 'erd4'), '\n')

