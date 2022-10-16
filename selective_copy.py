"""
Walk through a directory tree and search for file/s with
certain file extension. Copy file/s to a new directory.

For further improvement:
- ask user to input the path to search for the files.
- ask user to input the destination path of the files.
- path validation
"""
import os
import shutil
from pathlib import Path

check_path = Path.home() / 'selective_copy'
destination_path = Path.home() / 'destination_folder'

# Add user input for file extensions.
file_extension = input("File extensions/s(complete with dot[.] character), separated by space: ")

# Save file extensions in list.
file_extensions = file_extension.split()

if file_extensions:

    # Loop through directory, sub-directory and files then
    # copy each file with the same extension in file_extensions list
    # to a new folder.
    for folder_name, sub_folders, file_names in os.walk(check_path):
        for file_name in file_names:
            file_name_extension = Path(file_name)
            if file_name_extension.suffix in file_extensions:
                shutil.copy(check_path / file_name, destination_path)
                print(f"[{file_name}] COPIED TO {destination_path}.")
