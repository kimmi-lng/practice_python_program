#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
#empty list
list_numbs = []
#use try and except to ask for numbers and to set condition
while True:
    try:
        ask_numb = float(input("Enter a number: "))
        list_numbs.append(ask_numb)
    except ValueError:
        print("Invalid input")
        break
#print the result
print(f"The highest number is: {max(list_numbs)}")
