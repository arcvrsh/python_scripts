from sqlalchemy.orm import sessionmaker
from orm_file1 import Employee
from sqlalchemy import create_engine

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()


print("Welcome to Employeedb")
while True:
    print("***MENU***")
    print("1. Employees List")
    print("2. Add Employee")
    print('3.exit')
    op = input('Choose any option : ')

    if op == '1':
        results = sess.query(Employee).all()
        for emp in results:
            print("ID : ",emp.emp_id)
            print("Employee Name :",emp.emp_name)
            print("DOB :",emp.DOB)
            print()
    elif op == '2':
        print('Add new emp info')
        emp_name = input("Employee Name ->")
        DOB = input("DOB ->")
        salary = input("Salary ->")

        if emp_name and DOB and salary:
            salary = int(salary)

            obj = Employee(emp_name = emp_name,DOB = DOB,salary=salary)
            sess.add(obj)
            sess.commit()
            print("saved emp info")

    elif op == '3': 
        import sys
        sys.exit(0)
    else:
        print("wrong option, choose correct options")