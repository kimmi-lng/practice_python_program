#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
numbers = 0
while numbers <= 100:
    if numbers % 2 != 0:
        print(numbers)
    numbers += 1