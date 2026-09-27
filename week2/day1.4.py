# Ask the user for a number and print its multiplication table.

num = int(input("enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")