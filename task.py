
class Vehicle:
    """Базовый класс для всех транспортных средств."""

    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация транспортного средства.

        :param make: Марка производителя
        :param model: Модель
        :param year: Год выпуска
        """
        self._make = make
        self._model = model
        self._year = year
        self._mileage = 0  # Пробег в км (инкапсулирован, т.к. изменяется только через методы)

    @property
    def make(self) -> str:
        """Марка транспортного средства (только для чтения)."""
        return self._make

    @property
    def model(self) -> str:
        """Модель транспортного средства (только для чтения)."""
        return self._model

    @property
    def year(self) -> int:
        """Год выпуска (только для чтения)."""
        return self._year

    @property
    def mileage(self) -> int:
        """Текущий пробег в км (только для чтения)."""
        return self._mileage

    def drive(self, distance: int) -> None:
        """
        Увеличивает пробег транспортного средства.

        :param distance: Расстояние в км
        :raises ValueError: Если distance <= 0
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        self._mileage += distance

    def get_info(self) -> str:
        """Возвращает основную информацию о транспортном средстве."""
        return f"{self.make} {self.model} ({self.year})"

    def __str__(self) -> str:
        return f"Транспортное средство: {self.get_info()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year!r})"


class Car(Vehicle):
    """Класс легкового автомобиля."""

    def __init__(self, make: str, model: str, year: int, fuel_type: str):
        """
        Инициализация автомобиля.

        :param fuel_type: Тип топлива (бензин/дизель/электро)
        """
        super().__init__(make, model, year)
        self._fuel_type = fuel_type
        self._passengers = 0  # Текущее количество пассажиров

    @property
    def fuel_type(self) -> str:
        """Тип топлива автомобиля."""
        return self._fuel_type

    def add_passenger(self) -> None:
        """Добавляет одного пассажира (максимум 5)."""
        if self._passengers >= 5:
            raise ValueError("Превышено максимальное количество пассажиров")
        self._passengers += 1

    def remove_passenger(self) -> None:
        """Удаляет одного пассажира (не может быть меньше 0)."""
        if self._passengers <= 0:
            raise ValueError("В автомобиле нет пассажиров")
        self._passengers -= 1

    def get_info(self) -> str:
        """
        Перегрузка метода для добавления информации о топливе.
        (Причина перегрузки: нужно добавить специфичную для автомобиля информацию)
        """
        return f"{super().get_info()}, топливо: {self.fuel_type}"

    def __repr__(self) -> str:
        """Перегрузка repr для отображения типа топлива."""
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, " \
               f"year={self.year!r}, fuel_type={self.fuel_type!r})"


# Пример использования
if __name__ == "__main__":
    vehicle = Vehicle("ГАЗ", "Волга", 1985)
    print(vehicle)  # Транспортное средство: ГАЗ Волга (1985)
    print(repr(vehicle))  # Vehicle(make='ГАЗ', model='Волга', year=1985)

    car = Car("Toyota", "Camry", 2020, "бензин")
    car.drive(150)
    print(car.get_info())  # Toyota Camry (2020), топливо: бензин
    print(repr(car))  # Car(make='Toyota', model='Camry', year=2020, fuel_type='бензин')
