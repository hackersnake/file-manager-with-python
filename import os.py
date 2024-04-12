import os
import shutil
from tkinter import Tk, Label, Button, filedialog

def organize_files(directory_path):
    # Dictionary to map file extensions to their respective folders
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.ppt'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'CSV': ['.csv'],
        'Text': ['.txt'],
        'Music': ['.mp3', '.wav', '.flac'],
        # Add more file types as needed
    }

    # Iterate through files in the specified directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, file_extension = os.path.splitext(filename)

        # Determine the type of the file and move it to the appropriate folder
        moved = False
        for file_type, extensions in file_types.items():
            if file_extension.lower() in extensions:
                destination_folder = os.path.join(directory_path, file_type)
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                moved = True
                break

        # If file type is not predefined, create a folder for that extension
        if not moved:
            extension_folder = os.path.join(directory_path, file_extension[1:].lower())
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)
            shutil.move(file_path, os.path.join(extension_folder, filename))

def browse_button():
    directory_path = filedialog.askdirectory()
    organize_files(directory_path)
    status_label.config(text=f"Files in '{directory_path}' organized successfully!")

# GUI setup
root = Tk()
root.title("File Organizer")

label = Label(root, text="Click the button to select a directory for file organization:")
label.pack(pady=10)

browse_button = Button(root, text="Browse", command=browse_button)
browse_button.pack(pady=10)

status_label = Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
