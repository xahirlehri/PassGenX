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

if __name__ == "__main__":
    original_password = input("Enter a password: ")
    leet_password = leet_speak(original_password)
    print("Leet Speak Password:", leet_password)
