#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
#add variable maybe so that we can just change all lowered case into upper case without asking for users inputs
statement = "saNa All BALIW meOw mEow"
#add an empty variable so that it can hold the changed char
new_case = ""
#a loop to check each char
for char in statement:
    if 'a' <= char <= 'z':
        upp_case = chr(ord(char) - 32)
        new_case += upp_case
    else:
        new_case += char
#then print result
print(f"Original: {statement}")
print(f"Result: {new_case}")
