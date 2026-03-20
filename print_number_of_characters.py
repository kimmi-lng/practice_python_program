#Prog08: Create a program that ask the user to input their fullname. Print the number of characters in the input.
#Example:
#Input: Juan Dela Cruz
#Output: 14
#ask for their full name
#condiiton
ask_name = input("Enter your full name: ")
count = len(ask_name)
if ask_name.strip():
    print(f"Character count: {count}")
else:
    print("Invalid, No character found")