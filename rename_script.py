import os

# Specify the directory containing the files
directory = './cards'

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Split the filename into name and extension
    name, extension = os.path.splitext(filename)
    # Find the position of the first hyphen
    hyphen_position = name.find('-')
    # If a hyphen is found, construct the new filename
    if hyphen_position != -1:
        new_name = name[:hyphen_position].strip() + extension
        # Construct full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} -> {new_name}')

