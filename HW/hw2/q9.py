'''
String Manipulation Challenge: Password Validator
Create a Python program that validates a password based on specific criteria.

The password must meet the following criteria:

At least 8 characters long
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one digit
Contains at least one special character from @#$%^&*!
Does not contain spaces

'''

password = input("Enter a password: ")

if len(password) < 8:
    print("Password must be at least 8 characters long.")
    exit()  # Exit the program if the password is too short

if not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")    
    exit()  # Exit the program if the password does not contain an uppercase letter

if not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter.")
    exit()  # Exit the program if the password does not contain a lowercase letter

if not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")
    exit()  # Exit the program if the password does not contain a digit

if not any(char.isalnum() for char in password):
    print("Password must contain at least one special character.")
    exit()  # Exit the program if the password does not contain a special character

if ' ' in password:
    print("Password cannot contain spaces.")
    exit()  # Exit the program if the password contains spaces

print("Password is valid.") 