#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
#this function remove the space characters from right
#first add a variable with stored sting statement or just a term with space at right part
word = "Russel          "
#we will start from last index to identify the location of the characters
index = len(word) - 1
#use while loop to look continuously
while index >= 0 and word[index] == " ":
    index -= 1
#then use result as variable to store the result
result = word[:index + 1]
#print result
print(f"Original: |{word}|")
print(f"Result: |{result}|")


