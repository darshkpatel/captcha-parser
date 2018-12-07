from PIL import Image
import pytesseract
import argparse
import cv2
import os
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="path to input image to be OCR")
args = vars(ap.parse_args())
img = cv2.imread(args["image"],0)
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, img)
text = pytesseract.image_to_string(Image.open(filename), config='--psm 8')
print(text)
