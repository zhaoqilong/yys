#coding:utf-8
'''
brew install tesseract
pip install pytesseract
'''
import pytesseract
from PIL import Image
import cv2 as cv
# open image
image = Image.open('./yys_mark/' + 'tupo_ticket_61e08bf1.png')
code = pytesseract.image_to_string(image)
print(code)