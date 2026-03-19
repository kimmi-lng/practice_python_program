#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
numbers = []
#ask for numbers
for i in range(10):
    numb = float(input(f"Enter number {i+1}: "))
#condition
    numbers.append(numb)
for vals in numbers:
    if numbers.count(vals) == 1:
#add also maybe an empty list
#print results
        print(vals)
