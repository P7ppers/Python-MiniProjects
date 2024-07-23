# -*- coding: utf-8 -*-

#author - paarth mahajan made 7/22/2024

"""
Make an Employment Management System that
1) inserts employee record
2) display all employee records
3) search for employee records
4) update employee record
5) delete employee record
6) exit

Employee record contain Employee ID, Name, Department Name, and salary
"""
#mini porjects aims to work with dictionaries and their methods in python
#project details provided by - IITKanpur IFACET Summer Training Program

#Initializing data structures and variables

emp_mngmt_system = {}
emp_temp_record = {}
exit_program = False
choice = 0
menu_prompt = "\nEmployment Management System:\n\
1) insert employee record\n\
2) display all employee records\n\
3) search for employee records\n\
4) update employee record\n\
5) delete employee record\n\
6) exit\n"
update_prompt = "\nUpdate Information: \n1)Name\n2)Department\n3)Salary\n4)Updates done"

while (exit_program != True):
    print(menu_prompt)
    choice = int(input('Please enter the integer option you wish to choose: '))
    if choice == 1: #Code to add a fresh employee record
        emp_id = int(input("Enter your employee id: "))
        emp_name = (input("Enter your employee name: "))
        emp_dep = (input("Enter your employee department name: "))
        emp_salary = int(input("Enter your employee salary: "))
        emp_temp_record = {"Name":emp_name, "Department" : emp_dep, "Salary" : emp_salary}
        emp_mngmt_system.update({emp_id:emp_temp_record})
        print("Record successfully added!")
    elif choice == 2: #Displaying all employee records
        system_record = emp_mngmt_system.copy()
        for i in range(len(system_record)):
            record = system_record.popitem()
            print(i+1, "-> Employee ID: %d, Name: %s, Deparment: %s, Salary: %d "%(record[0], record[1]["Name"],record[1]["Department"],record[1]["Salary"]))
    elif choice == 3: #Displaying Specific employee record
        emp_id = int(input("Enter employee id for the record you want to search: "))
        record = emp_mngmt_system.get(emp_id)
        print("Employee ID: %d, Name: %s, Deparment: %s, Salary: %d "%(emp_id, record["Name"],record["Department"],record["Salary"]))
    elif choice == 4: #Updating employee info
        emp_id = int(input("Enter your employee id: "))
        emp_ids = emp_mngmt_system.keys()
        if emp_id not in emp_ids:
            print("Existing record not found! Please insert a employee record first")
        else:
            print("Record found. Proceeding with update.")
            emp_temp_record = emp_mngmt_system[emp_id]
            emp_name, emp_dep, emp_salary = emp_temp_record["Name"], emp_temp_record["Department"], emp_temp_record["Salary"]
            while (True):
                print(update_prompt)
                upd_choice = int(input("Please enter update parameter number: "))
                if upd_choice==1:
                    emp_name = (input("Enter your employee name: "))
                elif upd_choice ==2:
                    emp_dep = (input("Enter your employee department name: "))
                elif upd_choice==3:
                    emp_salary = int(input("Enter your employee salary: "))
                elif upd_choice == 4:
                    break
            emp_temp_record.update({"Name":emp_name, "Department" : emp_dep, "Salary" : emp_salary})
            emp_mngmt_system.update({emp_id:emp_temp_record})
            print("Your record has been successfully updated!")
    elif choice == 5: #Deleting employee record
        emp_id = int(input("Enter your employee id: "))
        emp_ids = emp_mngmt_system.keys()
        if emp_id not in emp_ids:
            print("Given employee id not found.")
        else:
            print("Employee id found. Deleting employee record...")
            del emp_mngmt_system[emp_id]
    elif choice == 6: #Exiting program
        print("Exiting Program...")
        exit_program = True
    else:
        print('Please enter a correct option number out of the menu.')
