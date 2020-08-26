from datetime import datetime



#Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы,
# с которыми вызвалась и возвращаемое значение.

#Написать декоратор из п.1, но с параметром – путь к логам.

print(datetime.now().date())
print(datetime.now().time())
#имя функции,

# аргументы,

# возвращаемое значение


# #Проброс параметров
# def x70(old_function):
#     def new_function(*args, **kwargs ):
#         something = old_function(*args, **kwargs
#         )
#         something = something * 70
#         return something
#     return new_function
#
# @x70
# def foo(*args, **kwargs ):
#     ...
#     return something