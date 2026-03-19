#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
#stores even numbers
all_even_numbers = []
#ask for 10 numbers
for i in range(10):
    numbers = float(input(f"Enter the number {i+1}: "))
#condition
    if numbers % 2 == 0:
        all_even_numbers.append(numbers)
#print how many are even numbers
print(len(all_even_numbers), "is/are even number/s.")