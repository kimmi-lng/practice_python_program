#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
#this functions does two things only, it is to capitalize the first letter the swap all the other to lower case
#first is to add a variable where the statement will be stored
statement = "saNa All BALIW meOw mEow"
#then use if else statement to identify if the variable is valid to do the conditions, then condition follows
if len(statement) > 0:
    first_character = statement[0].upper()
    other_characters = statement[1:].lower()
    full_statement = first_character + other_characters
#print result
print(f"Result: {full_statement}")