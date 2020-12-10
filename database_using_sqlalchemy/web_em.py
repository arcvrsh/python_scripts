from sqlalchemy.orm import sessionmaker
from orm_file1 import Employee
from sqlalchemy import create_engine

import streamlit as st

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

choice = st.sidebar.selectbox("select option",['Add employee','Employees list'])

if choice == 'Add employee':
    st.header("Add employee details")
    emp_name = st.text_input('enter employee name',)
    DOB = st.date_input('enter DOB ')
    salary = st.number_input('salary of publishing',min_value=25000,max_value=80000,value=30000)
    submit = st.button("save details")
    if submit and emp_name and DOB:
        obj = Employee(emp_name=emp_name, DOB = DOB,salary = salary)
        sess.add(obj)
        sess.commit()
        st.success("employee data added")
    elif emp_name or DOB or salary:
        st.warning("please fill valid details")
elif choice =='Employees list':
    st.header("Displaying all games")
    results = sess.query(Employee).all()
    for employee in results:
        st.subheader(employee.emp_name)
        st.text(employee.DOB)
        st.text(employee.salary)
        st.empty()

