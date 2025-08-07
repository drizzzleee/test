def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2  # Целочисленное деление
        guess = list[mid]
        if guess == item:        # Если элемент найден
            return mid
        if guess > item:         # Ищем в левой половине
            high = mid - 1
        else:                    # Ищем в правой половине
            low = mid + 1
    return None  # Элемент не найден

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 9))  # Выведет 1 (индекс числа 3)
