#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
#create an empty list
all_numbers = []
#identify all the needs
for numbers in range(0,101):
    if numbers % 10 != 0:
        all_numbers.append(numbers)
#in a list
print("numbers that doesn't end with 0 are:", all_numbers)
#ascending
for numbers in all_numbers:
    print(numbers)