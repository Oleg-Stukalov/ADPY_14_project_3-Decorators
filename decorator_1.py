from datetime import datetime
from collections import OrderedDict
import json


#Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы,
# с которыми вызвалась и возвращаемое значение.

def decor_logger(param=None):
    LOG = OrderedDict()
    LOGFILE = 'log.json'

    def _decor_logger(old_function):
        def new_function(*args, **kwargs):
            print('Количество лог записей: ', len(LOG))
            date = str(datetime.now().date())
            time = str(datetime.now().time())
            key = (f'Date: {date}, Time: {time}, Function name: {old_function.__name__}, Args: {str(args)}, Kwargs: {str(kwargs)};')
            print('Key:', key)
            result = LOG.get(key)
            # сохранение результата в файл
            with open(LOGFILE, 'w', encoding='utf-8') as f:
                json.dump(key, f, ensure_ascii=False, indent=4)
            print('Список стран со ссылками Википедии успешно сохранен в локальный файл:', LOGFILE)
            #print(LOG)
            print(LOGFILE)
            #return result
        return new_function
    return _decor_logger




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