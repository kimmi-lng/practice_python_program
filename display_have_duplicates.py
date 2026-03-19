#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
#empty list
numbers = []
duplicated_numbers = []
#ask for numbers
for i in range(10):
    ask_number = float(input(f"Enter a number {i+1}: "))
    numbers.append(ask_number)
for vals in numbers:
    if numbers.count(vals) > 1:
        duplicated_numbers.append(vals)
#print result
print("Numbers that has duplicate: ", duplicated_numbers)
