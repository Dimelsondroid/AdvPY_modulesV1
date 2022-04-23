from datetime import datetime

from Application.salary import *
from Application.DB.people import *

if __name__ == '__main__':
    print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    get_employees()
    calculate_salary()
    pass