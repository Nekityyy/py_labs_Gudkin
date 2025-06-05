# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=","):
    # Разделяем строки на списки участников
    list1 = group1.split(delimiter)
    list2 = group2.split(delimiter)

    # Находим пересечение множеств и сортируем результат
    common = sorted(set(list1) & set(list2))
    return common
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    delimiter="|"
)

print("Общие участники:", common_participants)