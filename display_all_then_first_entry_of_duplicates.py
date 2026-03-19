#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
numbers = []
for i in range(10):
    numbs = float(input(f"Enter number {i+1}: "))
    if numbs not in numbers:
        numbers.append(numbs)
print(numbers)