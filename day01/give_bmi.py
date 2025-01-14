# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# User input for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI using the function
result = calculate_bmi(weight, height)
print("Your BMI is:", result)

# Interpretation of BMI categories
if result < 18.5:
    print("You are underweight.")
elif 18.5 <= result <= 24.9:
    print("You have a normal weight.")
elif 25 <= result <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")