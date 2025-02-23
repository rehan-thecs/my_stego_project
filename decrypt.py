import cv2
import os
import string

# Load the encrypted image
img = cv2.imread("encryptedImage.jpg")

if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Load stored password
try:
    with open("password.txt", "r") as f:
        stored_password = f.read().strip()
except FileNotFoundError:
    print("Error: Password file not found. Cannot decrypt!")
    exit()

# Ask for password
pas = input("Enter passcode for Decryption: ")

# Check password
if pas != stored_password:
    print("YOU ARE NOT AUTHORIZED!")
    exit()

# Character mappings
c = {i: chr(i) for i in range(256)}

# Initialize decryption
message = ""
n, m, z = 0, 0, 0
height, width, _ = img.shape

# Decrypt the message
while n < height and m < width:
    char = c.get(img[n, m, z], None)
    if char is None or char == "\0":  # Stop at NULL terminator
        break
    message += char
    
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= width:
            m = 0
            n += 1

print("Decryption message:", message)
