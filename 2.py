import random
import string

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Example use:
print(generate_password(16))  # makes a 16-character password
