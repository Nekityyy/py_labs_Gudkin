
from task_1 import Book, Car, BankAccount

if __name__ == "__main__":
    # Создаем экземпляры классов с корректными данными
    book = Book("1984", "George Orwell", 328)
    car = Car("Toyota", 220, 100)
    account = BankAccount("1234567890", 1000.0)

    # Проверяем методы с корректными аргументами
    print(f"Книга объемная? {book.is_long_book()}")
    print(f"Время чтения: {book.get_reading_time(40)} часов")

    car.accelerate(50)
    print(f"Текущая скорость: {car.current_speed} км/ч")
    print(f"Время поездки: {car.get_travel_time(220)} часов")

    account.deposit(500.0)
    print(f"Баланс после пополнения: {account.get_balance()}")
    print(f"Снято со счета: {account.withdraw(300.0)}")

    # Проверяем обработку исключений
    try:
        # Неправильный тип данных для количества страниц (должно быть int)
        book.get_reading_time("50")  # передаем строку вместо числа
    except TypeError:
        print('Ошибка: неправильные данные (ожидается int для pages_per_hour)')

    try:
        # Отрицательное увеличение скорости
        car.accelerate(-50)  # отрицательное значение
    except ValueError:
        print('Ошибка: увеличение скорости должно быть положительным')

    try:
        # Попытка снять больше денег, чем есть на счете
        account.withdraw(2000.0)  # недостаточно средств
    except ValueError:
        print('Ошибка: недостаточно средств на счете')

    try:
        # Неправильный тип данных для номера счета (должен содержать только цифры)
        invalid_account = BankAccount("ABC123", 1000.0)
    except ValueError:
        print('Ошибка: номер счета должен содержать только цифры')

    try:
        # Отрицательный баланс при создании счета
        invalid_account = BankAccount("1234567890", -100.0)
    except ValueError:
        print('Ошибка: баланс не может быть отрицательным')






