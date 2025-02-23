import cv2
import os
import string

img = cv2.imread("rehan.jpg") 

if img is None:
    print("Error: Image file not found!")
    exit()

msg = input("Enter secret message: ") + "\0"
password = input("Enter a passcode: ")


with open("password.txt", "w") as f:
    f.write(password)


d = {chr(i): i for i in range(256)}


n, m, z = 0, 0, 0
height, width, _ = img.shape

for char in msg:
    if n >= height or m >= width:
        print("Error: Message is too long for the image!")
        exit()

    img[n, m, z] = d[char]
    
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= width:
            m = 0
            n += 1


cv2.imwrite("encryptedImage.jpg", img)
print("Encryption completed. Encrypted image saved as 'encryptedImage.jpg'.")
