from datetime import datetime
# from Application import salary
# from Application.DB import people
from Application.salary import calculate_salary
from Application.DB.people import get_employees

if __name__ == '__main__':
    print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    calculate_salary()
    get_employees()
    pass