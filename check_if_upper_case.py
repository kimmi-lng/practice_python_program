#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
#first ask for a statement or a string
ask_statement = input("Enter a statement (this check if what you'll enter are all capitalized: ")
upper_case = True
existing = False
#check these string if all are in upper case if it is it returns true
#check if in lower case then it returns false
for i in ask_statement:
    if 'a' <= i <= 'z':
        upper_case = False
        break
    if 'A' <= i <= 'Z':
        existing = True
#print results
if upper_case and existing:
    print("All are capitalized")
else:
    print("All/some are not capitalized")