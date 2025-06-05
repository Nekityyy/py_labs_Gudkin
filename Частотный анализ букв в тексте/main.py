# TODO  Напишите функцию count_letters
def count_letters(text):
    letter_counts = {}
    order = []  # Для сохранения порядка появления букв
    for char in text.lower():
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
                order.append(char)
    return letter_counts, order

def calculate_frequency(letter_counts):
    total_letters = sum(letter_counts.values())
    return {letter: round(count / total_letters, 2)
            for letter, count in letter_counts.items()}
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
# Подсчет букв (возвращаем и словарь, и порядок букв)
counts, letter_order = count_letters(main_str)
frequencies = calculate_frequency(counts)

# Вывод результатов в порядке появления букв
for letter in letter_order:
    print(f"{letter}: {frequencies[letter]:.2f}")