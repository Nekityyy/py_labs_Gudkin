import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        if not author:
            raise ValueError("Автор книги не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def is_long_book(self) -> bool:
        """
        Проверка, является ли книга объемной (более 300 страниц).

        :return: Является ли книга объемной

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.is_long_book()
        True
        """
        return self.pages > 300

    def get_reading_time(self, pages_per_hour: int = 50) -> float:
        """
        Рассчитывает примерное время прочтения книги в часах.

        :param pages_per_hour: Количество страниц, прочитываемых за час (по умолчанию 50)
        :return: Время прочтения в часах

        :raise ValueError: Если pages_per_hour <= 0

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_reading_time(40)
        8.2
        """
        if not isinstance(pages_per_hour, int):
            raise TypeError("Количество страниц в час должно быть типа int")
        if pages_per_hour <= 0:
            raise ValueError("Количество страниц в час должно быть положительным числом")
        return round(self.pages / pages_per_hour, 2)


class Car:
    def __init__(self, brand: str, max_speed: int, current_speed: int = 0):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param max_speed: Максимальная скорость автомобиля (км/ч)
        :param current_speed: Текущая скорость автомобиля (км/ч, по умолчанию 0)

        Примеры:
        >>> car = Car("Toyota", 220)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть типа str")
        if not brand:
            raise ValueError("Марка автомобиля не может быть пустой")
        self.brand = brand

        if not isinstance(max_speed, int):
            raise TypeError("Максимальная скорость должна быть типа int")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self.max_speed = max_speed

        if not isinstance(current_speed, int):
            raise TypeError("Текущая скорость должна быть типа int")
        if current_speed < 0:
            raise ValueError("Текущая скорость не может быть отрицательной")
        if current_speed > max_speed:
            raise ValueError("Текущая скорость не может превышать максимальную")
        self.current_speed = current_speed

    def accelerate(self, speed_increase: int) -> None:
        """
        Увеличение скорости автомобиля.

        :param speed_increase: На сколько км/ч увеличить скорость
        :raise ValueError: Если увеличение скорости приводит к превышению максимальной скорости

        Примеры:
        >>> car = Car("Toyota", 220, 100)
        >>> car.accelerate(50)
        """
        if not isinstance(speed_increase, int):
            raise TypeError("Увеличение скорости должно быть типа int")
        if speed_increase <= 0:
            raise ValueError("Увеличение скорости должно быть положительным числом")
        if self.current_speed + speed_increase > self.max_speed:
            raise ValueError("Превышение максимальной скорости автомобиля")
        self.current_speed += speed_increase

    def get_travel_time(self, distance: float) -> float:
        """
        Рассчитывает время в часах для преодоления расстояния на текущей скорости.

        :param distance: Расстояние в км
        :return: Время в часах

        :raise ValueError: Если расстояние <= 0 или текущая скорость == 0

        Примеры:
        >>> car = Car("Toyota", 220, 110)
        >>> car.get_travel_time(220)
        2.0
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        if self.current_speed == 0:
            raise ValueError("Автомобиль стоит на месте")
        return round(distance / self.current_speed, 2)


class BankAccount:
    def __init__(self, account_number: str, balance: float = 0.0):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param account_number: Номер счета
        :param balance: Текущий баланс (по умолчанию 0.0)

        Примеры:
        >>> account = BankAccount("1234567890", 1000.0)
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть типа str")
        if not account_number.isdigit():
            raise ValueError("Номер счета должен содержать только цифры")
        self.account_number = account_number

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть типа int или float")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        """
        Внесение средств на счет.

        :param amount: Сумма для внесения
        :raise ValueError: Если сумма <= 0

        Примеры:
        >>> account = BankAccount("1234567890", 1000.0)
        >>> account.deposit(500.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительным числом")
        self.balance += amount

    def withdraw(self, amount: float) -> float:
        """
        Снятие средств со счета.

        :param amount: Сумма для снятия
        :return: Реально снятая сумма
        :raise ValueError: Если сумма <= 0 или недостаточно средств

        Примеры:
        >>> account = BankAccount("1234567890", 1000.0)
        >>> account.withdraw(300.0)
        300.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительным числом")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= amount
        return amount

    def get_balance(self) -> float:
        """
        Получение текущего баланса.

        :return: Текущий баланс

        Примеры:
        >>> account = BankAccount("1234567890", 1000.0)
        >>> account.get_balance()
        1000.0
        """
        return self.balance


if __name__ == "__main__":
    doctest.testmod()


