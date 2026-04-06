#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
#time consuming if ill use the users input so maybe ill just add the fixed text
nickname = "Russel"
#add or store the target width for the justify
targ_width = 15
#set condition
subtract = max(0,targ_width - len(nickname))
result = nickname + (subtract*" ")
#print result
print(f"Result: |{result}|, with total length of {len(result)}")