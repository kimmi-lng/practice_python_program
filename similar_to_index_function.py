#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
#to mimic this function we will be using 2 variable at first to store the whole statement and also the word that need to be found
statement = "saNa All BALIW meOw mEow"
want_index = "BALIW"
#get their len so that we can identify how many index are there
statement_length = len(statement)
want_index_length = len(want_index)
#using for loop to find the strings and the index or the range
found_index = -1
for i in range (statement_length - want_index_length + 1):
    if statement[i:i+want_index_length] == want_index:
        found_index = i
        break
#then print the result
if found_index != -1: #using is else to print if false
    print(f"Found index: {found_index}")
else:
    print(f"Could not find index: {want_index}")