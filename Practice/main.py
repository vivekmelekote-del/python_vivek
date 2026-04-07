from Chat_GPT_OPPS_PROBLEMS import Employee

employee_salary = Employee("A471479","Vivek", 1841000)

class GetEmployeeSalary:
    def print_salary(self):
        print(employee_salary.annual_salary)

get_salary = GetEmployeeSalary()

get_salary.print_salary()

print(employee_salary.annual_salary())