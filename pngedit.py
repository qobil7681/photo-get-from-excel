import os
from PIL import Image
import numpy as np

def find_horizontal_separators(img_arr):
    horizontal_sum = img_arr.mean(axis=2).sum(axis=1)
    normalized_sum = (horizontal_sum - min(horizontal_sum)) / (max(horizontal_sum) - min(horizontal_sum))
    threshold = normalized_sum.mean() / 4
    separator_indices = np.where(normalized_sum < threshold)[0]
    return separator_indices

def extract_portraits(img_arr, separators):
    portraits = []
    current_start = 0
    for i, sep in enumerate(separators):
        if i > 0 and (sep - separators[i-1]) < 10:
            continue
        portraits.append(img_arr[current_start:sep])
        current_start = sep
    portraits.append(img_arr[current_start:])
    return portraits

def save_portraits(portraits, output_dir='photos'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_files = []
    for i, portrait in enumerate(portraits):
        portrait_img = Image.fromarray(portrait)
        # Images will be saved as '1.png', '2.png', ...
        output_file_path = os.path.join(output_dir, f'{i+1}.png')
        portrait_img.save(output_file_path)
        output_files.append(output_file_path)
    return output_files

def main(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    separators = find_horizontal_separators(img_array)
    portraits = extract_portraits(img_array, separators)
    files = save_portraits(portraits)
    print(f"Saved {len(files)} portraits in the 'photos' directory with numeric filenames starting from 1:")

    for file in files:
        print(file)

if __name__ == "__main__":
    img_path = 'rasmlar.png'  # Replace with your image path
    main(img_path)
