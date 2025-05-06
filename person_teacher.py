# Base class Person
class Person:
    def __init__(self, name, age):
        """
        Initializes a person with a name and age.
        :param name: The name of the person
        :param age: The age of the person
        """
        self.name = name
        self.age = age
    
    def display_info(self):
        """Displays the person's name and age."""
        print(f"Name: {self.name}, Age: {self.age}")

# Derived class Teacher (inherits from Person)
class Teacher(Person):
    def __init__(self, name, age, subject):
        """
        Initializes a teacher with a name, age, and subject.
        :param name: The teacher's name
        :param age: The teacher's age
        :param subject: The subject the teacher teaches
        """
        # Call the parent class (Person) constructor
        super().__init__(name, age)
        self.subject = subject
    
    def display_info(self):
        """Displays the teacher's information including the subject they teach."""
        # Call the parent class method to display name and age
        super().display_info()
        print(f"Subject: {self.subject}")

# Example usage
if __name__ == "__main__":
    # Create a Person object
    person = Person("Alice", 30)
    print("Person Information:")
    person.display_info()
    
    print("\n")
    
    # Create a Teacher object
    teacher = Teacher("Mr. Smith", 45, "Mathematics")
    print("Teacher Information:")
    teacher.display_info()
