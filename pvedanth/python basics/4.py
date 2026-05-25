# Define the local and Global variables with the same name and print both variables and understand the scope of the variables
global_var = "I am a global variable"

def my_function():
    local_var = "I am a local variable"
    print("Inside function - Global Variable:", global_var)
    print("Inside function - Local Variable:", local_var)

my_function()
print("Outside function - Global Variable:", global_var)