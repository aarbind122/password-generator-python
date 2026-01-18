import random
import string

length = int(input("Enter password length: "))

use_upper = input("Include uppercase letters? (y/n): ")
use_digits = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

chars = string.ascii_lowercase

if use_upper == 'y':
    chars += string.ascii_uppercase
if use_digits == 'y':
    chars += string.digits
if use_symbols == 'y':
    chars += string.punctuation

password = ""
for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)
