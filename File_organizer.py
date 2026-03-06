import os
import shutil

folder = "test_folder"

images_folder = os.path.join(folder, "Images")
documents_folder = os.path.join(folder, "Documents")

# create folders if they don't exist
os.makedirs(images_folder, exist_ok=True)
os.makedirs(documents_folder, exist_ok=True)

for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):

        if file.endswith(".jpg"):
            shutil.move(file_path, os.path.join(images_folder, file))

        elif file.endswith(".pdf"):
            shutil.move(file_path, os.path.join(documents_folder, file))

print("Files organized successfully!")