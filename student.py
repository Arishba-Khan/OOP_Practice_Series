# Student class definition
class Student:
    def __init__(self, name, marks):
        # Initialize the student's name and marks
        self.name = name
        self.marks = marks
    
    def display(self):
        # Display the student's name and marks
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")

# Main block to demonstrate class functionality
if __name__ == "__main__":
    # Creating instances of the Student class
    student1 = Student("Alice", 95)
    student1.display()  # Display details for Alice
    
    student2 = Student("Bob", 87)
    student2.display()  # Display details for Bob
