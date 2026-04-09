#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
#first defining the variable, better if its given that asking for users input
statement = "saNa All BALIW meOw mEow"
targ_index = "All"
#using len function to count how long was the text and the need to find
statement_length = len(statement)
targ_index_length = len(targ_index)
#set condition
found_index = -1
position = statement_length - targ_index_length
for i in range(position, -1, -1):
    if statement[i :i + targ_index_length] == targ_index:
        found_index = i
        break
#print result
if found_index != -1:
    print(f"Found index: {found_index}")
else:
    print(f"Could not find index: {targ_index}")