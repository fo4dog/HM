# Task 1

def convert_time(duration: int) -> str:
    days = duration // 86400
    hours = (duration // 3600) % 24
    minutes = (duration // 60) % 60
    seconds = duration % 60
    if days != 0:
        Time = f'{days} дн {hours} час {minutes} мин {seconds} сек'
    elif hours != 0:
        Time = f'{hours} час {minutes} мин {seconds} сек'
    elif minutes != 0:
        Time = f'{minutes} мин {seconds} сек'
    else:
        Time = f'{seconds} сек'

    return Time


duration = 400153
result = convert_time(duration)
print(result)

# Task 2a

def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    sum = 0
    for number in dataset:
        sum_of_digits = 0
        for i in range(len(str(number))):
            sum_of_digits += int(str(number)[i])
        if sum_of_digits % 7 == 0:
            sum += number
    return sum

# Task 2b

def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
            сумма цифр которых делится нацело на 7"""
    dataset_plus_17 = [number + 17 for number in dataset]
    sum = 0
    for number in dataset_plus_17:
        sum_of_digits = 0
        for i in range(len(str(number))):
            sum_of_digits += int(str(number)[i])
        if sum_of_digits % 7 == 0:
            sum += number
    return sum

# Task 2c

def sum_list_3(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    sum = 0
    for number in dataset:
        sum_of_digits = 0
        number_plus_17 = number + 17
        for i in range(len(str(number_plus_17))):
            sum_of_digits += int(str(number_plus_17)[i])
        if sum_of_digits % 7 == 0:
            sum += number_plus_17
    return sum


my_list = [number ** 3 for number in range(1001) if number % 2 == 1]  # Соберите нужный список по заданию
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
result_3 = sum_list_3(my_list)
print(result_3)

# Task 3

def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    if number % 10 == 1 and number != 11:
        new_string = f'{number} процент'
    elif 1 < number % 10 < 5 and (number < 11 or number > 14):
        new_string = f'{number} процента'
    else:
        new_string = f'{number} процентов'
    return new_string


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
print(type(24//7))