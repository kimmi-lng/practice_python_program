#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.
#first is to define variable
comp_text_with_suffix = "Kim Russel jr"
suffix = " jr"
#get the length of the suffix to be removed
length_suffix = len(suffix)
#condition
if length_suffix > 0 and comp_text_with_suffix[-length_suffix:] == suffix:
    result = comp_text_with_suffix[:-length_suffix]
else:
    result = comp_text_with_suffix
#print result
print(result)