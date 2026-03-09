#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
all_even = []
for numbers in range(0,101):
    if numbers % 2 == 0:
        all_even.append(numbers)
print(all_even, "are all even number")

for numbers in range(0,101):
    if numbers % 2 == 0:
        print(f"{numbers} is even")