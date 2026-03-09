#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

number = int(input("Enter the first number: "))
number /= float (input("Enter the second number: "))
# use / for normal division with decimals not // because that is for floor division
print(number, "is the quotient of this two numbers")