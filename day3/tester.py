from S1E7 import Baratheon, Lannister

# Creating a Baratheon character: Robert
Robert = Baratheon("Robert")
print(Robert.__dict__)  # Print attributes
print(Robert.__str__())  # String representation
print(Robert.__repr__())  # Formal representation
print(Robert.is_alive)  # Check if alive
Robert.die()  # Mark as deceased
print(Robert.is_alive)  # Check again
print(Robert.__doc__)  # Display class docstring

print("---")

# Creating a Lannister character: Cersei
Cersei = Lannister("Cersei")
print(Cersei.__dict__)  # Print attributes
print(Cersei.__str__())  # String representation
print(Cersei.is_alive)  # Check if alive

print("---")

# Creating a Lannister using the class method
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name: {Jaine.first_name}, Family: {Jaine.family_name}, Alive: {Jaine.is_alive}")
