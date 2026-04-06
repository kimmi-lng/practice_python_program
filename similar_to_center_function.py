#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
#first is to set our variable
nickname = "Russel"
targ_width = 15
#set condition for left and right spaces to center the text
total_spaces = targ_width - len(nickname)
if total_spaces > 0:
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    result = (" " * left_spaces) + nickname + (" " * right_spaces)
else:
    result = nickname
#print result
print(f"Result: |{result}|")
