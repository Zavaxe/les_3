# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код
month = 0
gen_expenses = expenses
year_grant = educational_grant * 10
while month <= 9:
    month += 1
    new_expenses = expenses + expenses * 0.03
    expenses = new_expenses
    gen_expenses += new_expenses
parents_money = gen_expenses - year_grant
print('Студенту надо попросить', int(parents_money), 'рублей')