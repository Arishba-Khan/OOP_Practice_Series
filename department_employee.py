# Employee class represents an individual employee
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        """Display the employee's ID and name."""
        print(f"Employee ID: {self.employee_id}, Name: {self.name}")


# Department class contains a collection of employees
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # This list holds Employee objects

    def add_employee(self, employee):
        """Add an employee to the department."""
        self.employees.append(employee)
        print(f"Employee {employee.name} added to {self.name} department")

    def remove_employee(self, employee_id):
        """Remove an employee by ID from the department."""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                print(f"Employee {employee.name} removed from {self.name} department")
                return
        print(f"Employee with ID {employee_id} not found in {self.name} department")

    def display_employees(self):
        """Display all employees in the department."""
        print(f"\nEmployees in {self.name} department:")
        if not self.employees:
            print("No employees in this department")
        else:
            for employee in self.employees:
                employee.display_info()


# Example usage
if __name__ == "__main__":
    # Create independent Employee objects
    emp1 = Employee("John Doe", "E001")
    emp2 = Employee("Jane Smith", "E002")
    emp3 = Employee("Bob Johnson", "E003")

    # Create Department objects
    hr_dept = Department("Human Resources")
    it_dept = Department("Information Technology")

    # Add employees to departments (aggregation: employees exist independently)
    hr_dept.add_employee(emp1)
    hr_dept.add_employee(emp2)
    it_dept.add_employee(emp3)

    # Display all employees in each department
    hr_dept.display_employees()
    it_dept.display_employees()

    # Move employee from HR to IT
    hr_dept.remove_employee("E002")
    it_dept.add_employee(emp2)

    # Show updated department employees
    hr_dept.display_employees()
    it_dept.display_employees()

    # Show that employees still exist independently of departments
    print("\nEmployees still exist independently:")
    emp1.display_info()
    emp2.display_info()
    emp3.display_info()
