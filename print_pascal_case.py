#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuanDelaCruz
#first casing need to be fixed then maybe replace() to replace space characters
ask_name = input("Enter your full name in incorrect casing: ")
pascal_case = ask_name.title().replace(" ", "")
if pascal_case.strip():
    print(f"The entered name in pascal case is: {pascal_case}")
else:
    print("Invalid input, must be something")