from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""

    str_out = ''
    for i in list_in: # не понял в чем могла быть проблема с выводом, возможно я ее просмотрел
        i = str(i)
        i = i.split('.')
        str_out += f'{i[0]} руб {i[1].ljust(2, "0")} коп, '
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    print(f'id до  сортировки {id(list_in)}') # id до сортировки
    list_in.sort()
    print(f'id после  сортировки {id(list_in)}') # id после сортировки
    return list_in


# id до сортировки 2259229114176
result_2 = sort_prices(my_list)
# id после сортировки2259229114176
print(f'Список после сортировки по возрастанию цены: {result_2}')


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    # пишите реализацию здесь
    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(f'Новый список цен по убыванию: {result_3}')


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_in.sort()
    list_out = list_in[-5:]
    return list_out


result_4 = check_five_max_elements(my_list)
print(f'Пять самых высоких цен: {result_4}')
