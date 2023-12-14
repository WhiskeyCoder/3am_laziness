import os
import zipfile

directory = "C:\FOLDER\FOLDER\FOLDER"

for file in os.listdir(directory):
    folder_path = os.path.join(directory, file)
    zip_file = zipfile.ZipFile(file + ".zip", 'w')
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            zip_file.write(os.path.join(root, file))
    zip_file.close()
  print("well... that was easy") 
