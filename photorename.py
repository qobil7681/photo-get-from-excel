import os

def rename_photos(directory_path, name_file_path):
    # Read names from name.txt file
    with open(name_file_path, 'r') as file:
        names = file.readlines()

    # Iterate over files in directory
    with open(name_file_path, 'r') as file:
        for i, line in enumerate(file):
            filename = f"{i+1}.png"
            if filename in os.listdir(directory_path):
                # Get the corresponding name from names list
                new_name = line.strip() + '.png'
                # Construct old and new paths
                old_path = os.path.join(directory_path, filename)
                new_path = os.path.join(directory_path, new_name)
                # Rename the file
                os.rename(old_path, new_path)
                print(f'Renamed {filename} to {new_name}')

# Example usage:
directory_path = 'photos'
name_file_path = 'jeton.txt'
rename_photos(directory_path, name_file_path)
