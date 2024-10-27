salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 1.03  # Ежемесячный рост цен

month = 0 # текущий месяц
money_capital = 0 # Необходимая подушка безопасности до расчета

while month < months:
    money_capital += spend
    money_capital -= salary  # Расчет подушки безопасности
    spend *= increase        # Прирости цен
    month += 1               # Переход к следующему месяцу

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",  int(round(money_capital, 0)))
