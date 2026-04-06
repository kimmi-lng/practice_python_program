#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
#we can create an empty list the store here each of the words so that they can be modified
statement = "saNa All BALIW meOw mEow"
#split the statement
cut_words = statement.split()
new_statement = []
#condition using for loop
for word in cut_words:
    new_words = word[0].upper() + word[1:].lower()
    new_statement.append(new_words)
result = " ".join(new_statement)
#print the result
print(f"Original: {result}")
print(f"Result: {result}")