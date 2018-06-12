from PIL import Image
import pytesseract
import argparse
import cv2
import os

image = cv2.imread('C://Users//Win10//a.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('C://Users//Win10//b.png', gray)

size = 7680, 4320
#size = 7016, 4961
im = Image.open('C://Users//Win10//b.png')
im_resized = im.resize(size, Image.ANTIALIAS)
im_resized.save('C://Users//Win10//c.png', "PNG")

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)//Tesseract-OCR//tesseract'
text = pytesseract.image_to_string(Image.open('C://Users//Win10//c.png'))
print(text)

