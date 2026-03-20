#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
#ask for a string
ask_statement = input("Please enter your statement/words to convert capitals to lowercase: ")
lowered_case = ""
#then convert those capitalized string using its ascii values
for i in ask_statement:
    if 'A' <= i <= 'Z':
        lowered_char = chr(ord(i) + 32)
        lowered_case += lowered_char
    else:
        lowered_case += i
#print results
print(f"Lowered case: {lowered_case}")