#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
#empty list
list_numbers = []
#condition try and exept maybe to continously ask for numbers then
while True:
    try:
        ask_numb = float(input("Enter a number: "))
        list_numbers.append(ask_numb)
    except ValueError:
        most_dup_number = max((list_numbers), key=list_numbers.count)
        print ("Invalid input")
#print result
        print("Numbers that has most duplicate: ", most_dup_number)
        break
