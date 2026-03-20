#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
#an empty list to be sorted
list_numbs = []
#add condition use while True then try and except to identify value
while True:
    try:
        ask_numb = float(input("Enter a number: "))
        list_numbs.append(ask_numb)
    except ValueError:
        print("Invalid input")
        break
list_numbs.sort(reverse=True)
#print the result from highest to lowest
print(f"The list from highest to lowest: {list_numbs}")
