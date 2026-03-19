#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
#create an empty list
all_numbers_not_ends_zero_or_five = []
#identify all the needs
for numbers in range(0,101):
    if numbers % 10 != 0 and numbers % 5 != 0:
        all_numbers_not_ends_zero_or_five.append(numbers)
#ascending
for numbers in all_numbers_not_ends_zero_or_five:
    print(numbers)