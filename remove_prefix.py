#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
#ask for the full name with the prefix
ask_name = input("Please enter your name with the prefix: ")
#ask for the prefix that needs to be removed
prefix = input("Please enter your prefix that needs to be removed: ")
#condition
if ask_name.startswith(prefix):
    ask_name = ask_name[len(prefix):]
else:
    ask_name = ask_name
#print result
print(ask_name)


