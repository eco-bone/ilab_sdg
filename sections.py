import os

# Define the target folder
folder_name = "Chapter_VI"  # Change this to your desired folder name

# Define the range of chapters
start = 100
end = 146

# Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

# Create empty .md files inside the folder
for i in range(start, end + 1):
    file_path = os.path.join(folder_name, f"Chapter_{i}.md")
    open(file_path, "w").close()  # Creates an empty file

print(f"Empty Markdown files created successfully inside '{folder_name}'!")
