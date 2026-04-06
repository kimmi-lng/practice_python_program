#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
#users input also the suffix that needs to be removed
statement = input("Enter a name/statement: ")
suffix = input("Enter the suffix: ")
#variable to store the suffix
lenght_suffix = len(suffix)
#condition
if lenght_suffix > 0:
    result = statement[-lenght_suffix:] == suffix
else:
    result = True
#print result
print(result)