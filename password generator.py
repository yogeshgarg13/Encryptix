import random
import string

def generate_password(length, has_uppercase, has_numbers, has_special_chars):
  password = ''
  characters = string.ascii_lowercase

  if has_uppercase:
    characters += string.ascii_uppercase
  if has_numbers:
    characters += string.digits
  if has_special_chars:
    characters += string.punctuation

  for _ in range(length):
    password += random.choice(characters)

  return password

def main():
  print("Password Generator")
  print("----------------")

  length = int(input("Enter the desired length of the password: "))

  has_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
  has_numbers = input("Include numbers? (y/n): ").lower() == 'y'
  has_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

  password = generate_password(length, has_uppercase, has_numbers, has_special_chars)

  print("Generated Password:", password)

if __name__ == "__main__":
  main()
