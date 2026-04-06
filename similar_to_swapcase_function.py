#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
#add two variable which is the text and the empty one for storing
statement = "SaNa All BALIW meOw mEow"
swap_case = ""
#add else if condition to check whether it is in upper case or lower case vise versa
for char in statement:
    if char.isupper():
        swap_case += char.lower()
    elif char.islower():
        swap_case += char.upper()
    else:
        swap_case += char
#print the result
print(f"Original: {statement}")
print(f"Result: {swap_case}")