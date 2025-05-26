numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
# 1. Находим индекс пропущенного элемента
missing_index = numbers.index(None)

# 2. Создаем копию списка без пропущенного элемента
numbers_without_none = [num for num in numbers if num is not None]

# 3. Вычисляем среднее арифметическое оставшихся элементов
average = sum(numbers_without_none) / len(numbers)  # len(numbers) включает пропуск

# 4. Заменяем пропущенный элемент
numbers[missing_index] = average

# 5. Выводим результат
print("Измененный список:", numbers)
