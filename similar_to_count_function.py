#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
#we will be needing counter here to mimic the count function
occurences = 0
counters = 0
#start with 2 given variables the given statement where to look the 2nd variable that needs to be count
statement = "mono naka naka ah ah naka"
targ_text = "naka"
#usign len function we can count the length of the statement
statement_length = len(statement)
targ_text_length = len(targ_text)
#starting out loop with while loop to compare
while counters <= statement_length - targ_text_length:
    if statement[counters : counters + targ_text_length] == targ_text:
        occurences += 1
        counters += 1 # to not overlap
    else:
        counters += 1
#print the result
print(f"Original text:{statement}, and Target text:{targ_text}")
print(f"Count:{occurences}")