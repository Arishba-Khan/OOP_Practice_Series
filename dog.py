class Dog:
    def __init__(self, name, breed):
        """
        Initializes a Dog object with a name and breed.
        :param name: The name of the dog
        :param breed: The breed of the dog
        """
        self.name = name
        self.breed = breed
    
    # Instance method to make the dog bark
    def bark(self):
        """
        Makes the dog bark.
        """
        print(f"{self.name} says: Woof! Woof!")
    
    # Instance method to display dog's information
    def display_info(self):
        """
        Displays the dog's name and breed.
        """
        print(f"Name: {self.name}, Breed: {self.breed}")
    
    # Instance method to make the dog play a certain activity
    def play(self, activity):
        """
        Makes the dog play a specific activity.
        :param activity: The activity the dog is playing (e.g., fetch, frisbee)
        """
        print(f"{self.name} is playing {activity}")

# Example usage
if __name__ == "__main__":
    # Create dog objects
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Max", "German Shepherd")
    
    # Call instance methods on dog1
    print("Dog 1's details:")
    dog1.display_info()
    dog1.bark()
    dog1.play("fetch")
    
    print("\n")
    
    # Call instance methods on dog2
    print("Dog 2's details:")
    dog2.display_info()
    dog2.bark()
    dog2.play("frisbee")
