import os
import shutil

# Define the file types and their corresponding directories
FILE_TYPES = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

def organize_files(directory):
    # Create directories if they don't exist
    for dir_name in FILE_TYPES.keys():
        dir_path = os.path.join(directory, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Move files to their corresponding directories
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            moved = False
            for dir_name, extensions in FILE_TYPES.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, dir_name, filename))
                    moved = True
                    print(f"Moved '{filename}' to '{dir_name}'")
                    break
            
            if not moved:
                shutil.move(file_path, os.path.join(directory, "Others", filename))
                print(f"Moved '{filename}' to 'Others'")

if __name__ == "__main__":
    directory = input("Enter the directory path to organize: ")
    organize_files(directory)
