#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
#Example:
#Input:         Juan Dela Cruz
#Output: Juan Dela Cruz
#use lstrip function to remove the space before the strings
user_name = input("Enter your name with several space character at the beginning: ")
name = user_name.lstrip()
print(name)


