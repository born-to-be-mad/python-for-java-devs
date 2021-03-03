class employee:
    numberOfEmployees = 0

    # default constructor
    def __init__(self):
        self.name = ""
        self.salary = 0.0
        employee.numberOfEmployees += 1

    # overloaded constructor with all parameters
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee.numberOfEmployees += 1

    def displayCount(self):
        print("Total number of employees " + employee.numberOfEmployees)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp1 = employee("Dzmitry", 1500)
emp2 = employee("Ivan", 3500)

emp1.displayEmployee()
emp2.displayEmployee()

print("Total number of employees: " + str(employee.numberOfEmployees))
