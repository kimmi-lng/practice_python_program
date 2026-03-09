#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
#ask for the numbers in a loop
all_numbers = []
for i in range(10):
    numbers = float(input(f"Enter the number {i+1}: "))
#check how many are ood numbers
    if numbers%2 != 0:
        all_numbers.append(numbers)
#print the result
print(f"{len(all_numbers)}x is/are odd numbers")
