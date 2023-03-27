import os

# Set the directory path here
directory = r"C:\Users\nicks\Downloads\webp"

# Loop through all files in the directory with the .webp extension
for filename in os.listdir(directory):
    if filename.endswith(".webp"):
        # Replace any dashes in the filename with spaces
        alt_text = filename.replace("-", " ")[:-5]
        # Create the HTML <img> tag with alt and title attributes
        img_tag = f'<img src="{filename}" alt="{alt_text}" title="{alt_text}">'
        # Print the tag to the console
        print(img_tag)
