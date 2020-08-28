from datetime import datetime
from collections import OrderedDict
import json


#Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы,
# с которыми вызвалась и возвращаемое значение.

def decor_logger(param=None):
    #LOG = OrderedDict()
    LOGFILE = 'log.json'
    log_entry = None

    with open(LOGFILE, 'w', encoding='utf-8') as f:
        json.dump([], f)

    def _decor_logger(old_function):
        def new_function(*args, **kwargs):
            #print('Количество лог записей: ', len(LOG))
            date = str(datetime.now().date())
            time = str(datetime.now().time())
            log_entry = f'Date: {date}, Time: {time}, Function name: {old_function.__name__}, Args: {str(args)}, Kwargs: {str(kwargs)};'
            print('***', type(log_entry))
            print('В лог будет сохранена следующая запись: ', log_entry)
            #result = LOG.get(key)
            # сохранение результата в файл
            with open(LOGFILE, 'a', encoding='utf-8') as f:
                json.dump(log_entry, f, ensure_ascii=False, indent=4)
                json.dump('\n', f, ensure_ascii=False, indent=4)
            print('Лог-запись успешно добавлена в локальный файл:', LOGFILE)
            #print(LOG)
            #return result
        return new_function
    return _decor_logger




@decor_logger()
def concat(str_1, str_2):
    return f'{str_1}{str_2}'
print(concat('abc', 'erd'), '\n')
print(concat('abc', 'erd1'), '\n')\

@decor_logger()
def concat(str_1, str_2):
    return f'{str_1}{str_2}'
print(concat('abc', 'erd'), '\n')
print(concat('abc', 'erd1'), '\n')





# # #кэширование ф-ий
# def cachable(param):
#     CACHE = OrderedDict()
#
#     def _cachable(old_function):
#
#         def new_function(*args, **kwargs):
#             print(len(CACHE))
#             key = (old_function.__name__, str(args), str(kwargs))
#             result = CACHE.get(key)
#             if result is not None:
#                 return result
#             else:
#                 result = old_function(*args, **kwargs)
#                 CACHE[key] = result
#                 if len(CACHE) > param:
#                     CACHE.popitem(last=False)
#                 return result
#
#         return new_function
#
#     return _cachable