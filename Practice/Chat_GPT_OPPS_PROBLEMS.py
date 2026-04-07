class Employee:
    
    def __init__(self, emp_id, emp_name, emp_salary):
        self.id = emp_id
        self.name = emp_name
        self.salary = emp_salary
        self.base_salary = 0
        self.epb = 0
        self.age = 0
    
    def annual_salary(self):
        total_monthly_take_home = 0
        total_monthly_take_home = self.salary / 12
        total_monthly_take_home -= (self.get_pf() + (self.get_tax()/12))
        return f"The total monthly take home is: {total_monthly_take_home}"


    def get_pf(self):
        return ((self.calculate_base_salary() ) / 8.33)
    
    def calculate_base_salary(self):
        return ((self.salary * 50) / (12 * 100))
    
    def new_tax_calculation(self):
        tax_total = 0
        if ((self.salary - 75000) <= 400000):
            tax_total += 0
        if ((self.salary - 75000) >= 800000):
            tax_total += (self.salary - 475000 * .05) 
        if ((self.salary - 75000) >= 1200000):
            tax_total += (self.salary - 875000 * .10) 
        if ((self.salary - 75000) >= 1600000):
            tax_total += (self.salary - 1275000 * .15) 
        if ((self.salary - 75000) >= 2000000):
            print("HI")
            tax_total += (self.salary - 1675000 * .20) 
        if ((self.salary - 75000) >= 2400000):
            tax_total += (self.salary - 2075000 * .25)
        if (self.salary > 2400000):
            tax_total += (self.salary - 2475000 * .30)
        print(f"Total Tax is: {tax_total/12}")
        return tax_total
    
    # def tax_based_on_age(self):
    #     if(self.age > 60 and self.age < 80):
    #         if(self.salary >= 300000):
    #             self.salary -= 300000
    #     if(self.age > 80):
    #         if(self.salary >= 500000):
    #             self.salary -= 500000

    def old_tax_calculation(self):
        total_tax = 0
        print("Sorry!!\nThis feture is under development")
        return


    def get_tax(self):
        tax_scheme = input("Are you planning to go with 'New' or 'Old regime'?: \n").lower()
        if(tax_scheme == "new"):
            return self.new_tax_calculation()
        elif (tax_scheme == "old"):
            return self.old_tax_calculation()