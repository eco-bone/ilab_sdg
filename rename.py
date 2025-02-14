import os

# Define the target folder
folder_name = "Chapter_VI"  # Change this if needed

# Iterate through all files in the folder
for file_name in os.listdir(folder_name):
    if file_name.startswith("Chapter_") and file_name.endswith(".md"):
        new_name = file_name.replace("Chapter_", "Section_")
        old_path = os.path.join(folder_name, file_name)
        new_path = os.path.join(folder_name, new_name)
        os.rename(old_path, new_path)

print("Files renamed successfully!")
