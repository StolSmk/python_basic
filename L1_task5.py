#5.	Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее
# сообщение.
#Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
proceeds = float(input('Input proceeds: '))
costs = float(input('Input costs: '))
results = proceeds - costs
if results > 0:
    print(f'Profit = {results}')
    print(f'Profitability = {results / proceeds}')
    staff = int(input('Input number of staff: '))
    print(f'Profit per employee = {results / staff}')
else:
    print(f'Loss = {results}')


