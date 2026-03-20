#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
index = 0
#ask user for the name with spaces before it
ask_name = input("Please enter your name with spaces before it: ")

while index < len(ask_name) and ask_name[index] == " ":
    index += 1

first_character = ask_name[index:]
print(first_character)

#set condition to find the first character
#use that index to get the range of that first string
#print result