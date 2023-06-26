import os

parent_folder = "V:\python\code"

if not os.path.exists(parent_folder):
    os.makedirs(parent_folder)

for letter in range(26):
    folder_name = chr(ord('a') + letter)
    folder_path = os.path.join(parent_folder, folder_name)
    os.makedirs(folder_path)