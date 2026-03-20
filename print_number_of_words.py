#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
#Example:
#Input: We will weather the weather whatever the weather whether we like it or not
#Output: 14
#use count() maybe i think lemme check
ask_statement = input("Enter a statement: ")
if ask_statement.strip():
    word_count = len(ask_statement.split())
    print(f"The number of word in the statement: {word_count}")
else:
    print("Invalid input, cannot be empty")