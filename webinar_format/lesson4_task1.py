"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv
script_name, hours, rate, premium = argv
print(f'An employee`s salary is: {hours} * {rate} + {premium}'
      f' = {float(hours) * float(rate) + float(premium)}')
