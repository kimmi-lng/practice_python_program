#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
#we will just again use the given statement so there is no need for users input
#for loop so that we can check each characters if they are in lower or upper case
#print result
statement = "saNa All BALIW meOw mEow"

has_upper = False # we can assume that they are false
has_lower = False

for char in statement:

    if 'A' <= char <= 'Z':
        has_upper = True
        break
    if 'a' <= char <= 'z':
        has_lower = True

if has_lower and not has_upper:
    decision = True
else:
    decision = False

print(f"{decision}")
