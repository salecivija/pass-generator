# Password Generator

This is a simple password generator script that creates a window with a button and a text field. When the button is clicked, it generates a random password and displays it in the text field.

## How to run the script

1. Install the required modules:

```bash
pip install PyQt5
```

2. Run the script:
```bash
python main.py
```

## How the password is generated

The password consists of 7 characters: 4 lowercase letters, 4 digits, and 3 uppercase letters. The characters are chosen at random using the random.choices() function from the random module.

The string module provides constants for the ASCII letters and digits: string.ascii_lowercase contains all lowercase letters, string.ascii_uppercase contains all uppercase letters, and string.digits contains all digits.

The generated password is then joined into a single string using the join() method and displayed in the text field using the setText() method.