def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    num_count=0
    try:
        for num in numbers:
            try:
                result += num
                num_count+=1
            except TypeError:
                incorrect_data += 1
        return (result, incorrect_data,num_count)
    except TypeError:
        print('Передан неверный тип данных')

def calculate_average(numbers):
    try:
        result=personal_sum(numbers)[0]/personal_sum(numbers)[2]
        return result
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('Передан неверный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
print(f'Результат 4: {calculate_average([])}')