# Write a method for increment and decrement operators(++, --)
def increment_decrement(num):
    incremented_value = num + 1  # Incrementing the number
    decremented_value = num - 1  # Decrementing the number
    
    return incremented_value, decremented_value
# Example usage
number = 10
results = increment_decrement(number)
print(f"Original number: {number}")
print(f"Incremented value: {results[0]}")
print(f"Decremented value: {results[1]}")
