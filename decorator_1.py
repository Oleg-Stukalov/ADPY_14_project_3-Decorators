from datetime import datetime
import json


def decor_logger(param=None):
    LOGFILE = 'log.json'
    #log_entry = None

    with open(LOGFILE, 'w', encoding='utf-8') as f:
        json.dump([], f)

    def new_function(*args, **kwargs):
        date = str(datetime.now().date())
        time = str(datetime.now().time())
        log_entry = f'Date: {date}, Time: {time}, Function name: {new_function.__name__}, Args: {str(args)}, Kwargs: {str(kwargs)};'
        #print('***', type(log_entry))
        print('В лог будет сохранена следующая запись: ', log_entry)
        # сохранение результата в файл
        with open(LOGFILE, 'a', encoding='utf-8') as f:
            json.dump(log_entry, f, ensure_ascii=False, indent=4)
            f.write('\n')
        print('Лог-запись успешно добавлена в локальный файл:', LOGFILE)
        return log_entry
    return new_function



@decor_logger
def concat(str_1, str_2):
    return f'{str_1}{str_2}'
print(concat('abc', 'erd'), '\n')
print(concat('abc', 'erd1'), '\n')
print(concat('abc', 'erd2'), '\n')
print(concat('abc', 'erd3'), '\n')
print(concat('abc', 'erd4'), '\n')







