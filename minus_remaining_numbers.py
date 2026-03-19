#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
#ask for the numbers
all_numbers = []
for i in range(10):
    numbers = float(input(f"Enter the number {i+1}: "))
    all_numbers.append(numbers)

difference = all_numbers[0] - sum(all_numbers[1:10])

print(f"The difference of {all_numbers[0]} and other numbers is {difference}")
