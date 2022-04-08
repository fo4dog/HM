def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = []
    for i in list_in:
        name = i.split()[-1].title()
        welcome_str = f'Привет, {name}'
        list_in.insert(list_in.index(i), welcome_str)
        list_in.remove(i)
    # for i in list_in:
    #     name = i.split()[-1].title()
    #     welcome_str = f'Привет, {name}'
    #     list_out.append(welcome_str)

    return list_in  # Задача решена без создания дополнительного списка


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)