# Define the Bank class
class Bank:
    # Class variable to hold the name of the bank (shared among all instances)
    bank_name = "Global Bank"
    
    def __init__(self, branch_name):
        """
        Initialize a Bank object with a branch name.
        :param branch_name: The name of the branch of the bank
        """
        self.branch_name = branch_name  # Instance variable for branch name
    
    def display_details(self):
        """
        Display the current bank name and branch name.
        """
        print(f"Bank: {Bank.bank_name}, Branch: {self.branch_name}")
    
    @classmethod
    def change_bank_name(cls, new_name):
        """
        Change the class-level bank name for all instances of the class.
        :param new_name: The new name of the bank
        """
        cls.bank_name = new_name  # Modify the class-level bank name
        print(f"Bank name changed to: {cls.bank_name}")

# Example usage: Create Bank objects and demonstrate functionality
if __name__ == "__main__":
    # Create two bank branches
    branch1 = Bank("Downtown")
    branch2 = Bank("Uptown")
    
    # Display initial details for both branches
    branch1.display_details()  # Output: Bank: Global Bank, Branch: Downtown
    branch2.display_details()  # Output: Bank: Global Bank, Branch: Uptown
    
    # Change the bank name using the class method
    Bank.change_bank_name("City Bank")
    
    # Display updated details - the change affects all instances
    branch1.display_details()  # Output: Bank: City Bank, Branch: Downtown
    branch2.display_details()  # Output: Bank: City Bank, Branch: Uptown
