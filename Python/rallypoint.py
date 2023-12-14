import os
import shutil

# Specify the main directory where you want to move the files
main_directory = r"C:\Users\User\Downloads\FilesInFolders"


# Loop through all subdirectories in the main directory
for root, _, files in os.walk(main_directory):
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(root, file)

        # Check if it's not the main directory itself
        if file_path != main_directory:
            try:
                # Move the file to the main directory
                shutil.move(file_path, main_directory)
                print(f"Moved {file} to {main_directory}")
            except Exception as e:
                print(f"Error moving {file}: {str(e)}")
