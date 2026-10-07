# Parent (Super) Class
class Animal:

    def speak(self):
        print("The animal makes a sound.")


# Child (Sub) Class inheriting from Animal
class Dog(Animal):

    # Overriding the speak method from the parent class
    def speak(self):
        print("The dog barks: Woof! Woof!")


# Creating an instance of the child class
my_dog = Dog()

# Calling the overridden method
my_dog.speak()