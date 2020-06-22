import sys
import os
from PIL import Image

# get args
img_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if the folder exists
if os.path.exists(img_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # loop through the folder files
    for filename in os.listdir(img_folder):
        img = Image.open(f'{img_folder}/{filename}')
        # split the text of the format (Ex: ('myfilename', '.jpg'))
        img_name = os.path.splitext(filename)[0]
        img.save(f'{output_folder}/{img_name}.png', 'png')
        print('Image converted')