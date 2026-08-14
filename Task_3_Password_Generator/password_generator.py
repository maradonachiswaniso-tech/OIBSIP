# Password Generator
# Task 3 - Beginner Tier

import random
import string

print("Password Generator")
print("-" * 30)

# Get password length
length = int(input("Enter password length (min 8): "))

# Make sure length is at least 8
if length < 8:
    print("Password must be at least 8 characters!")
    length = 8

# Generate password
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for i in range(length))

# Display password
print("Generated Password:", password)
print("Password length:", len(password))