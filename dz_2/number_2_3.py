def convert_list_in_str(list_in: list) -> str:
    str_out = ''
    # Task 2b
    # Получение строки из данного списка
    for i in list_in:  # добавление в начала числа 0, если в нем менее 2ух целочисленных разрядов
        if i.isdigit() == True and len(i) == 1:  # замена цифр без знака
            str_out += '"' + '0' + i + '" '
        elif (i.startswith('+') or i.startswith('-')) and len(i) == 2 and i[
                                                                          1:].isdigit() == True:  # замена цифр со знаком
            str_out += '"' + '+0' + i[1] + '" '
        elif i.isdigit() == True or (i.startswith('+') or i.startswith('-')):  # Поиск оставшихся чисел
            str_out += '"' + i + '" '
        else:
            str_out += i + ' '

    # Task 2a
    i = 0
    while True:
        if i == len(list_in):
            break
        if list_in[i].isdigit() is True and len(list_in[i]) == 1:  # замена цифр без знака

            number = list_in[i].zfill(2)
            list_in.remove(list_in[i])
            list_in.insert(i, f'{number}')
            list_in.insert(i + 1, '"')
            list_in.insert(i, '"')
            i += 2
        elif (list_in[i].startswith('+') or list_in[i].startswith('-')) and len(list_in[i]) == 2: # замена цифр со знаком
            number = list_in[i].zfill(3)
            list_in.remove(list_in[i])
            list_in.insert(i, f'{number}')
            list_in.insert(i + 1, '"')
            list_in.insert(i, '"')
            i += 2
        elif list_in[i].isdigit() is True or (list_in[i].startswith('+') or list_in[i].startswith('-')): # Поиск оставшихся чисел
            list_in.insert(i + 1, '"')
            list_in.insert(i, '"')
            i += 2
        i += 1
    # Если важно, чтобы строка получалась из нового списка
    str_out_2 = ''
    for i in list_in:
        if i.isdigit() or i.startswith('+'):
            str_out_2 += f'"{i}" '
        elif i != '"':
            str_out_2 += i + ' '
    print(list_in)  # вывод нового списка без использования нового списка
    print(str_out_2)  # Строка полученная из list_in после обработки
    return str_out  # Строка полученная из lits_in до обработки


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
