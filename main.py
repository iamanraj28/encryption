import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

#ENCRYPT

plain_text = input("Enter a message to encrypt: ")
encrypted_text = ""

for letter in plain_text:
    index = chars.index(letter)
    encrypted_text += key[index]

print(f"plain_text: {plain_text}")
print(f"encrypted_text: {encrypted_text}")

#DECRYPT

encrypted_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in encrypted_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted_text: {encrypted_text}")
print(f"plain_text: {plain_text}")
