#Prog04: Create a program that ask the user to input their fullname. Print the input in all lower case.
#Example:
#Input: Juan Dela Cruz
#Output: juan dela cruz
#ask for users name
ask_name = input("Enter your full name name: ")
#condition to check if its empty of what
if ask_name.strip():
    lowered_case = ask_name.lower()
#print
    print(f"The entered name in all lower case: {lowered_case}")
else:
    print("Invalid input, cannot be empty")
