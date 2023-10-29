def uppercase(func):
     def wrapper():
         original_result = func()
         modified_result = original_result.upper()
         return modified_result
     return wrapper
@uppercase
def  greet():
    return "hello"
def trace(func):
    def wrapper(*args, **kwargs):
        print(f'ТРАССИРОВКА: вызвана {func.__name__}() '
        f'с {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'ТРАССИРОВКА: {func.__name__}() '
        f'вернула {original_result!r}')
        return original_result
    return wrapper

import functools
#сохраняет метаданные о функции
def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

print(greet())