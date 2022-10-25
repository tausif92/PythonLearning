class Dog:
    # Class attribute: does not need self. This is already understood by pythin that it is a class attribute
    species = "mammal"
    def __init__(self, name, breed, spots, length):
        # Creating attributes of the class Dog
        # Take argument and assign it to self.attribute_name
        self.name = name
        self.breed = breed
        self.spots = spots
        self.length = length

    # If you want to return some string representation when the object of this class is called
    # Use __str__
    def __str__(self):
        return f"Dog name is {self.name} and breed is {self.breed}"

    # If you want to return something when the len(obj) is called, this block will be executed
    def __len__(self):
        return self.length

    # Methods are the functions defined in a class
    # Notice that the "number" is not the class/instance variable. Hence, we don't need self here.
    # Calling class variables/methods --> ClassName.variable
    # Calling instance variables/methods --> self.variable
    # Calling variables passed by user as in below method --> variable
    def bark(self, number):
        print(f"WOOF! My name is {self.name} and the number is {number}. My species is {Dog.species}")

# initialize Dog class with values
my_dog = Dog("Tommy", "Lab", False, 3)

print(my_dog.breed)
print(my_dog.spots)
print(my_dog.name)
print(type(my_dog))

my_dog.bark(5)

print(my_dog)  # Coming from __str__
print(len(my_dog))  # Coming from __len__

