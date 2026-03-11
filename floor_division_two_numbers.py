#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
#ask for two numbers
numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
#use the operation // to not include the decimal
result = numb1 // numb2
#print the result
print(f"The result of the division of this two numbers is {result}")