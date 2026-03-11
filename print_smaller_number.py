#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
#ask for 2 numbers
numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
#condition/compare
if numb1 < numb2:
#print the smaller number
    print(numb1, "is smaller than", numb2)
else:
    print(numb2, "is smaller than", numb1)
