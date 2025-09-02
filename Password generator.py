import string
import secrets
import re

def generate_password(length=16, nums=1, special_char=1, uppercase=1, lowercase=1):
    
    letters = string.ascii_letters
    symbols = string.punctuation
    numbers = string.digits
    
    all_characters = letters + symbols + numbers
    
    while True:
        password = ''
        for _ in range(length):
            password += secrets.choice(all_characters)
            
        constraints = [
            (nums, r'\d'),
            (special_char, '[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
            ]
            
        if all(
            constraint <= len(re.findall(pattern, password)) 
            for constraint, pattern in constraints
            ):
            break
        
    return password

password = generate_password()
print(f'Generated Password: {password}')
