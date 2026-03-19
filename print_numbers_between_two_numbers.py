#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
#create an empty list
numbers_between = []
#ask for two numbers
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
#set conditions
for i in range(number1 + 1, number2):
    numbers_between.append(i)
#print the result
print(numbers_between)