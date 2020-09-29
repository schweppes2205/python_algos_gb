"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple, defaultdict

company_data_pattern = namedtuple("Company",
                                  "name "
                                  "first_quarter_income "
                                  "second_quarter_income "
                                  "third_quarter_income "
                                  "fourth_quarter_income "
                                  "avg_income")

user_input_company_count = int(input("Please enter the amount of companies for input: "))
company_data = defaultdict(str)
for i in range(user_input_company_count):
    user_input_comp_name = input(f"#{i}. Please enter company name: ")
    user_input_comp_income = input(f"Please enter 4 digits for {user_input_comp_name} "
                                   f"as according income for 1-4 quarters: ").split(" ")
    income_int = list(map(int, user_input_comp_income))
    avg_income_tmp = sum(income_int)/len(income_int)
    company_data[i] = company_data_pattern(
        name=user_input_comp_name,
        first_quarter_income=user_input_comp_income[0],
        second_quarter_income=user_input_comp_income[1],
        third_quarter_income=user_input_comp_income[2],
        fourth_quarter_income=user_input_comp_income[3],
        avg_income=str(avg_income_tmp)
    )
avg_income_all_lst = []
for i in company_data.keys():
    avg_income_all_lst.append(int(company_data[i].first_quarter_income))
    avg_income_all_lst.append(int(company_data[i].second_quarter_income))
    avg_income_all_lst.append(int(company_data[i].third_quarter_income))
    avg_income_all_lst.append(int(company_data[i].fourth_quarter_income))
avg_income_all = sum(avg_income_all_lst)/len(avg_income_all_lst)
above_avg, below_avg = [], []
for i in company_data.keys():
    if float(company_data[i].avg_income) >= avg_income_all:
        above_avg.append(company_data[i].name)
    else:
        below_avg.append(company_data[i].name)
print("raw data:")
for i in company_data.keys():
    print(company_data[i])
print(f"overall avg: {avg_income_all}")
print(f"above avg: {above_avg}")
print(f"below avg: {below_avg}")
