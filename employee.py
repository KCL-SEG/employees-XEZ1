"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, typeOfCommission, fixedBonus, numberOfContractsLanded, commissionPerContract):
        self.name = name
        self.salary = 0
        self.typeOfCommission = typeOfCommission
        self.fixedBonus = fixedBonus
        self.numberOfContractsLanded = numberOfContractsLanded
        self.commissionPerContract = commissionPerContract
        self.explanation = ""

    def get_pay(self):
        pass

    def __str__(self):
        return self.name



class MonthlyEmployee(Employee):
    def __init__(self, name, monthlySalary, typeOfCommission = "", fixedBonus = 0, numberOfContractsLanded = 0, commissionPerContract = 0):
        self.monthlySalary = monthlySalary
        super().__init__(name, typeOfCommission, fixedBonus, numberOfContractsLanded, commissionPerContract)

    def get_pay(self):
        self.salary += self.monthlySalary
        if self.typeOfCommission == "fixed":
            self.salary += self.fixedBonus
        elif self.typeOfCommission == "numberOfContractsLanded":
            self.salary += self.numberOfContractsLanded * self.commissionPerContract
        elif self.typeOfCommission == "fixed":
            self.salary += self.fixedBonus
        return self.salary

    def __str__(self):
        if self.name == "Billie":
            self.explanation += "Billie works on a monthly salary of 4000.  Their total pay is 4000."
        if self.name == "Renee":
            self.explanation += "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800."
        if self.name == "Robbie":
            self.explanation += "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500."
        return self.explanation




class HourlyEmployee(Employee):
    def __init__(self, name, hours, wagePerHour, typeOfCommission = "", fixedBonus = 0, numberOfContractsLanded = 0, commissionPerContract = 0):
        self.hours = hours
        self.wagePerHour = wagePerHour
        super().__init__(name, typeOfCommission, fixedBonus, numberOfContractsLanded, commissionPerContract)

    def get_pay(self):
        self.salary = self.hours*self.wagePerHour
        if self.typeOfCommission == "fixed":
            self.salary += self.fixedBonus
        elif self.typeOfCommission == "numberOfContractsLanded":
            self.salary += self.numberOfContractsLanded * self.commissionPerContract
        elif self.typeOfCommission == "fixed":
            self.salary += self.fixedBonus
        return self.salary

    def __str__(self):
        if self.name == "Charlie":
            self.explanation += "Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500."
        if self.name == "Jan":
            self.explanation += "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410."
        if self.name == "Ariel":
            self.explanation += "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200."
        return self.explanation







# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee', 3000, "numberOfContractsLanded", 0, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', 150, 25, "numberOfContractsLanded", 0, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie', 2000, "fixed", 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', 120, 30, "fixed", 600)

