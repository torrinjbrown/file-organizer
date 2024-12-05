

import os
import glob
import shutil

source_f = r'sorucefile'
destination_f = r'filedestination'

# Ensure destination directory exists
os.makedirs(destination_f, exist_ok=True)

# Use os.path.join for pattern construction
pattern = os.path.join(source_f, '*.pdf')

# Use glob.glob to find all matching files
files = glob.glob(pattern)

for file in files:
    file_name = os.path.basename(file)  # Get the file name
    destination_path = os.path.join(destination_f, file_name)  # Construct destination path
    shutil.move(file, destination_path)  # Move the file
    print('Moved:', file, 'to', destination_path)

