from ft_calculator import Calculator

# Define two test vectors
a = [5, 10, 2]
b = [2, 4, 3]

# Test dot product
result_dot = Calculator.dotproduct(a, b)
print("Dot product is:", result_dot)  # Output: 56 (5*2 + 10*4 + 2*3)

# Test vector addition
result_add = Calculator.add_vec(a, b)
print("Add Vector is:", result_add)  # Output: [7, 14, 5]

# Test vector subtraction
result_sub = Calculator.sub_vec(a, b)
print("Sub Vector is:", result_sub)  # Output: [3, 6, -1]
