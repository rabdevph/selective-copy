import os
import shutil
from pathlib import Path

check_path = Path.home() / 'selective_copy'
destination_path = Path.home() / 'destination_folder'
file_extensions = ['.jpg']

for folder_name, sub_folders, file_names in os.walk(check_path):
    for file_name in file_names:
        file_name_extension = Path(file_name)
        if file_name_extension.suffix in file_extensions:
            shutil.copy(check_path / file_name, destination_path)
            print(f"[{file_name}] COPIED TO {destination_path}.")
