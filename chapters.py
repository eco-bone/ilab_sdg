import os

# Define the range of chapters
start = 4  # IV
end = 20   # XX

# Roman numerals mapping
roman_numerals = {
    4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII",
    9: "IX", 10: "X", 11: "XI", 12: "XII", 13: "XIII",
    14: "XIV", 15: "XV", 16: "XVI", 17: "XVII", 18: "XVIII",
    19: "XIX", 20: "XX"
}

# Create folders
for i in range(start, end + 1):
    folder_name = f"Chapter_{roman_numerals[i]}"
    os.makedirs(folder_name, exist_ok=True)

print("Folders created successfully!")