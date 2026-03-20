#Prog03: Create a program that ask the user to input their fullname. Print the input in all capital letter.
#Example:
#Input: Juan Dela Cruz
#Output: JUAN DELA CRUZ
#use try and except again maybe to differentiate values
ask_name = input("Enter a name: ")
if ask_name.strip():
    capitalized = ask_name.upper()
    print(f"The entered name in all capital: {capitalized}")
else:
    print("Invalid input, cannot be empty")