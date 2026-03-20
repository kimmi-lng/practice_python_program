#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
#Example:
#Input: 143
#Output: 000143
#ask for numbers
#condition
#print the result
try:
    ask_numbs = int(input("Enter a number (0-1000): "))
    if 0 <= ask_numbs <= 1000:
        print(f"The output is: {ask_numbs:06}")
    else:
        print("Enter a number that is within the range of 0 to 1000")
except ValueError:
    print("Invalid input")
