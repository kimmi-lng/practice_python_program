#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
#an empty list
list_numbs = []
#condition using while true and also try and except
while True:
    try:
        ask_numb = float(input("Enter a number: "))
        list_numbs.append(ask_numb)
    except ValueError:
        print("Invalid input")
        break
average = sum(list_numbs) / len(list_numbs)
#print the result
print(f"The average is: {average}")


