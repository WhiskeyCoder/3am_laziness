import os
import sys

directory = "C:\YOU_FOLDER"
if not os.path.exists(directory):
    print("Directory does not exist")
    sys.exit(1)

file_list = open("file_list.txt", "w")
for file in os.listdir(directory):
    file_list.write(file + "\n")

file_list.close()
