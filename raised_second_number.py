#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
#first number will be the base
base = float(input("Enter the first number (base): "))
#second number will be the exponent
exponent = float (input("Enter the second number (exponent): "))
#print the result
print(f"When {base} is raised to the power is {exponent} the result is {base ** exponent}")