#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
#empty set maybe
numb_list = []
#continously ask for number
while True:
#set condition maybe try and exempt
    try:
        ask_numb = float(input("Enter a number: "))
        numb_list.append(ask_numb)
    except ValueError:
        print("Invalid input")
        break
print(f"The lowest number is {min(numb_list)}")
