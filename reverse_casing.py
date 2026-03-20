#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuaN deLA cRuz
#will simply use swapcase iguess
ask_name = input("Enter your full name in incorrect casing: ")
if ask_name.strip():
    swap_casing = ask_name.swapcase()
    print(f"The entered name in all lower case: {swap_casing}")
else:
    print("Invalid input, cannot be empty")