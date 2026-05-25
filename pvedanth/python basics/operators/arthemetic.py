# Write a function for arithmetic operators(+,-,*,/)
def arithmetic_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "Division by zero is not allowed"
    
    return addition, subtraction, multiplication, division
# Example usage
num1 = 10
num2 = 5
results = arithmetic_operations(num1, num2)
print(f"Addition: {results[0]}")
print(f"Subtraction: {results[1]}")
print(f"Multiplication: {results[2]}")
print(f"Division: {results[3]}")
