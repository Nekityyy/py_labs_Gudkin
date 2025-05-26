money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
def calculate_months(money_capital, salary, spend, increase):
    months = 0
    current_capital = money_capital

    while True:
        # Проверяем, хватит ли денег на текущий месяц
        total_income = current_capital + salary
        if total_income < spend:
            break

        # Увеличиваем счетчик месяцев
        months += 1

        # Обновляем капитал (остаток после трат)
        current_capital = total_income - spend

        # Увеличиваем расходы на следующий месяц
        spend *= (1 + increase)

    return months


# Пример использования функции

months = calculate_months(money_capital, salary, spend, increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)
