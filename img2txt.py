import os
import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def process_images_in_folder(folder_path, output_file):
    with open(output_file, 'w') as outfile:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path) and file.lower().endswith(('.png', '.jpg', '.jpeg','.PNG', '.JPG', '.JPEG')):
                text = extract_text_from_image(file_path)
                outfile.write(f"Text extracted from {file}:\n")
                outfile.write(text)
                outfile.write("\n\n")
                print(f"Text extracted from {file}:")
                print(text)
                print("\n")

current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
folder_path = os.path.join(current_dir, 'images')

output_file = 'text.txt'

process_images_in_folder(folder_path, output_file)
