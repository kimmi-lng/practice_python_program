#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
all_numbers = []
for i in range(10):
    numbers = float (input(f"Enter number {i+1}: "))
    all_numbers.append(numbers)
total = sum(all_numbers)
print(f"The sum of all 10 numbers is: {total}")