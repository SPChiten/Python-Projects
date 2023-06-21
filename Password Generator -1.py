import random
import string

def generate_password(length, uppercase=True, lowercase=True, numbers=True, symbols=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = random.choices(characters, k=length)
    return ''.join(password)

# Example usage
password = generate_password(14)
print(password)