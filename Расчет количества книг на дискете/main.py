# TODO Найдите количество книг, которое можно разместить на дискете
# Исходные данные
floppy_size_mb = 1.44
pages = 100
lines = 50
chars = 25
char_size = 4

# 1. Рассчитываем размер одной книги в байтах
book_size_bytes = pages * lines * chars * char_size

# 2. Переводим размер дискеты в байты (1 Мб = 1024 Кб, 1 Кб = 1024 байт)
floppy_size_bytes = floppy_size_mb * 1024 * 1024

# 3. Вычисляем количество книг
num_books = int(floppy_size_bytes // book_size_bytes)
print("Количество книг, помещающихся на дискету:", num_books)
