import openpyxl
from PIL import Image
import io 
import os

def save_images_from_excel(excel_file, output_folder):
    # Load the Excel file
    wb = openpyxl.load_workbook(excel_file)
    
    # Ensure the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through each worksheet in the Excel file
    for sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]
        
        # Iterate through each image in the worksheet
        for idx, image in enumerate(sheet._images, start=1):
            # Get the image data
            image_data = image._data()
            
            # Create an Image object from the image data
            img = Image.open(io.BytesIO(image_data))
            
            # Construct the output file path
            output_file = f"{output_folder}/{idx}.png"
            
            # Save the image as PNG
            img.save(output_file, "PNG")

# Usage
excel_file = "bek.xlsx"
output_folder = "photos"
save_images_from_excel(excel_file, output_folder)
