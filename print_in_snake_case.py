#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
#Example:
#Input: jUAn DEla CrUZ
#Output: juan_dela_cruz
#use lower() to make all case snall then use replace() to replace space characters
ask_name = input("Enter your full name in incorrect casing: ")
snake_case = ask_name.lower().replace(" ", "_")
if ask_name.strip():
    print(f"The entered name in snake case is: {snake_case}")
else:
    print("Invalid input, must be somthing")