import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    salary = calculate_salary()
    employees = get_employees()
    print(f'У сотрудника "{employees}" за {datetime.date.today()} зарплата {salary} рублей')
    