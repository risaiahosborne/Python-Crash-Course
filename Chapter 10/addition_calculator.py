#Addition value error for strings instead of integers
#prompt the user to enter two numbers 
prompt = "Enter the first number: \nEnter 'q' to quit. "
prompt1 = "\nEnter the second number: \nEnter 'q' to quit. "
user_input = input(prompt)
user_input1 = input(prompt1)

# Using a while loop the inputs and convert them to integers
while True:
    if user_input == 'q' or user_input1 == 'q':
        break
    try:
        a = int(user_input)
        b = int(user_input1)
    except ValueError:
        print("Please enter two valid integers.")
        user_input = input(prompt)
        user_input1 = input(prompt1)
    else:
        print(f"The sum of {a} and {b} is {a + b}.")
        break
    
