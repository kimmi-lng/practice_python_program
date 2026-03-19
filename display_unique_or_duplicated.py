#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
#empty list
unique_numbers = []
#ask for numbers continously
while True:
    ask_numb = float(input("Enter a number: "))
#print duplicate if it has equal value
    if ask_numb in unique_numbers:
        print(f"The number {ask_numb} is duplicated")
        break
#print unique if numbers dont have equal value
    else:
        unique_numbers.append(ask_numb)
        print(f"The number {ask_numb} is unique")
#then print the list?
print("The list of all unique numbers: ",unique_numbers)
