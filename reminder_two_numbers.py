#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
#ask for two number
numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
#check the reminder
result = numb1 % numb2
print(f"The remainder of this two number is {result}")
#print the result