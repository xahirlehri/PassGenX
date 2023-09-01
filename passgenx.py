import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def leet_speak(text):
    leet_dict = {
        'a': '4',
        'b': '8',
        'e': '3',
        'g': '9',
        'i': '1',
        'o': '0',
        's': '$',
        't': '7',
        'h': '#'
    }

    leet_text = ''
    for char in text:
        if char.lower() in leet_dict:
            leet_text += leet_dict[char.lower()]
        else:
            leet_text += char

    return leet_text

def print_custom_logo():
    logo = """
\033[92m██████   █████  ███████ ███████  ██████  ███████ ███    ██ ██   ██ 
██   ██ ██   ██ ██      ██      ██       ██      ████   ██  ██ ██  
██████  ███████ ███████ ███████ ██   ███ █████   ██ ██  ██   ███   
██      ██   ██      ██      ██ ██    ██ ██      ██  ██ ██  ██ ██  
██      ██   ██ ███████ ███████  ██████  ███████ ██   ████ ██   ██ 
\033[0m
Created by Zahir Lehri | https://github.com/xahirlehri
"""
    print(logo)

def main_menu():
    show_logo = True  # Flag to track whether the logo has been shown

    while True:
        if show_logo:
            print_custom_logo()

        print("Main Menu:")
        print("1. Generate Password")
        print("2. Convert to Leet Speak")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            password_length = int(input("Enter the desired password length: "))
            generated_password = generate_password(password_length)
            print("Password Generated Successfully:")
            print(generated_password)
            input("Press Enter to continue...")  # Wait for user input
            show_logo = False  # Do not show the logo after Enter is pressed
        elif choice == '2':
            original_password = input("Enter a password: ")
            leet_password = leet_speak(original_password)
            print("Leet Speak Password:", leet_password)
            input("Press Enter to continue...")  # Wait for user input
            show_logo = False  # Do not show the logo after Enter is pressed
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
