#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
#will start with the given text already, no need for the users input
#to check the prefix it will have its own variable too
#using if else statement we can see or compare rather the given prefix to the texts
#then print the result
statement = "saNa All BALIW meOw mEow"
starts_with = "saNa"
#given the prefix we can use len function to find its index
count_prefix = len(starts_with)

if count_prefix == 0:
    decision = True
elif count_prefix > len(statement):
    decision = False
else:
    decision = statement[:count_prefix] == starts_with

print(f"Decision: {decision}") #a boolean is the result