#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
#starting  with two variable it may contain the main text or number string then the other contains the length of the target size
#then after, using el if statement, we can identify if we will be adding zeroes in front
#print result
numb_string = "123"
targ_length = 10
#to see how many zeroes to add
zeroes_add = targ_length - len(numb_string)
if zeroes_add > 0:
    result = (zeroes_add * "0") + numb_string
else:
    result = numb_string
print(f"Result:{result}")
