import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
bold_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

print("WELCOME TO PASSWORD GENERATOR!")
nr_small_letters = int(input("how many small letters do you wangt in your password? \n"))
nr_bold_letters = int (input("How many capital letters do you want in your password"))
nr_numbers = int (input("How many numbers do you want in your password? \n"))
nr_symbols = int (input("How many symbols do you want in your password? \n"))

password = ""

for char in range(0, nr_small_letters):
    password += random.choice(small_letters)
for char in range(0, nr_bold_letters):
    password += random.choice(bold_letters)
for char in range(0, nr_numbers):
    password += random.choice(numbers)
for char in range (0, nr_symbols):
    password += random.choice(symbols)

print(password)

