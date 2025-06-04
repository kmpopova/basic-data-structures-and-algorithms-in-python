"""
Task: Create a Python class named Person.

Attributes:
name (string)
age (integer)
occupation (string, optional, defaults to "Unemployed")

Methods:
__init__(self, name, age, occupation="Unemployed"): The constructor.
greet(self): Prints a greeting message, including the person's name and age (e.g., "Hello, my name is [name] and I am [age] years old.").
introduce_occupation(self): Prints a message with the occupation of the person.
is_adult(self): Returns True if the person is 18 or older, False otherwise.

Example Usage:
# Create a Person object
person1 = Person("Alice", 30, "Software Engineer")
person2 = Person("Bob", 16)
"""

class Person():
    def __init__(self, name: str, age: int, occupation="Unemployed"):
        self.name = name
        self.age = age
        self.occupation = occupation

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def introduce_occupation(self):
        if self.occupation != "Unemployed":
            print(f"I work as a {self.occupation}.")
            return f"I work as a {self.occupation}."
        else:
            print(f"I am {self.occupation}.")
            return f"I am {self.occupation}."

    def is_adult(self):
        return self.age > 18


if __name__ == "__main__":
    person1 = Person("Alice", 30, "Software Engineer")
    person2 = Person("Bob", 16)

    person1.greet()
    person1.introduce_occupation()

    person2.greet()
    person2.introduce_occupation()
    print(person1.is_adult())
    print(person2.is_adult())

"""
# Call methods
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
person2.greet()  # Output: Hello, my name is Bob and I am 16 years old.
person1.introduce_occupation()  # Output: I work as a Software Engineer.
person2.introduce_occupation() # Output: I am Unemployed.
print(person1.is_adult())  # Output: True
print(person2.is_adult())  # Output: False
"""