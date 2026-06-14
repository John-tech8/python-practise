class Employee:
    def __init__(self,name,emp_id,basic_salary):
        self.name=name
        self.emp_id=emp_id
        self.basic_salary=basic_salary


    def calculate_gross(self):
        hra=0.2*self.basic_salary
        da=0.1*self.basic_salary
        gross_salary=self.basic_salary+hra+da

        return gross_salary
    def display_details(self):
        print("Employee Name:",self.name)
        print("Employee id:",self.emp_id)
        print("Basic salary:",self.basic_salary)
        print("Gross Salary:",self.calculate_gross())


e1=Employee("Ram",69,30000)
e1.display_details()
