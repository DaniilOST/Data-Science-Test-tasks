from datetime import datetime

def date_difference(first_date, second_date):
    first_date = datetime.strptime(first_date, "%Y-%m-%d")
    second_date = datetime.strptime(second_date, "%Y-%m-%d")
    result = second_date - first_date
    return abs(result.days)

first_date = input("Введите первую дату (ГГГГ-ММ-ДД): ")
second_date = input("Введите вторую дату (ГГГГ-ММ-ДД): ")

print(date_difference(first_date, second_date))
