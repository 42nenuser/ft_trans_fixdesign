class Example:
    class_variable = 0  # Class-level variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # Instance-level variable

    def instance_method(self):
        # Access instance-level variable
        print(f"Instance variable: {self.instance_variable}")

    @classmethod
    def class_method(cls):
        # Access class-level variable
        print(f"Class variable: {cls.class_variable}")

    @staticmethod
    def static_method():
        # Static method does not have access to self or cls
        print("This is a static method and does not have access to self or cls.")

# Create an instance of the class
example_instance = Example(5)

# Access instance method
example_instance.instance_method()  # Output: Instance variable: 5

# Access class method
example_instance.class_method()  # Output: Class variable: 0

# Access static method
example_instance.static_method()  # Output: This is a static method and does not have access to self or cls.
