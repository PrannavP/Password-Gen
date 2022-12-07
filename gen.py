import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@$&./'

password = []

# ask user how much length he wants
genLength = int(input("Enter the length you want?: "))


def check_user_instruction():
    instruction = int(input("Please select the options: \n1. Only letters\n 2. Letters and Numbers\n 3. Letters, numbers and symbols: "))

    if(instruction == 1):
        generate_letters()
    elif(instruction == 2):
        generate_with_numbers()
    elif(instruction == 3):
        generate_with_all()
    else:
        print("Instruction not found")

# printing only letters
def generate_letters():
    for i in range(genLength):
        generatedPassword = random.choice(letters)

        password.append(generatedPassword)

    print("The random password is " + "".join(password))


def generate_with_numbers():
    for i in range(genLength):
        lettersAndNumbers = letters + numbers

        generatedPassword = random.choice(lettersAndNumbers)

        password.append(generatedPassword)

    print("The random password is " + "".join(password))

def generate_with_all():
    for i in range(genLength):
        lettersNumbersAndSymbols = letters + numbers + symbols

        generatedPassword = random.choice(lettersNumbersAndSymbols)

        password.append(generatedPassword)

    print("The random password is " + "".join(password))


check_user_instruction()