import random
import string

def generatePassword(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

   
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    if length < 4:
        print("Password length must be at least 4 characters.")
        return None

    password = random.choices(all_characters, k=length)

    password[0] = random.choice(uppercase_letters)
    password[1] = random.choice(lowercase_letters)
    password[2] = random.choice(digits)
    password[3] = random.choice(special_characters)

    random.shuffle(password)

    return ''.join(password)

try:
    password_length = int(input("Enter the length of the password: "))
    password = generatePassword(password_length)
    if password:
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a valid integer for the password length.")
