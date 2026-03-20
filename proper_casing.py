#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: Juan Dela Cruz
#ask for the name then use if else statement for condition then print
ask_name = input("Enter your full name: ")
if ask_name.strip():
    proper_casing = ask_name.title()
    print(f"The entered name in proper casing: {proper_casing}")
else:
    print("Invalid input, cannot be empty")