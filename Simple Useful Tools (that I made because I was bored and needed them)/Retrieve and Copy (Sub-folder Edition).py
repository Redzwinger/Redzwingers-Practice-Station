import os
import shutil

def copy_files(src_folder, dest_folder):
    
    # Iterating through all files and directories
    for root, dirs, files in os.walk(src_folder):
        
        # Reiterating through the files (Recursion Baby!)
        for file in files:
            src_path = os.path.join(root, file)
            dest_path = os.path.join(dest_folder, os.path.relpath(src_path, src_folder))
            
            # Creating directories and copying files
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy(src_path, dest_path)

if __name__ == "__main__":
    
    source_folder = input(" Enter the source folder path: ")
    destination_folder = input(" Enter the destination folder path: ")

    copy_files(source_folder, destination_folder)
    print(" Files copied successfully!")

# Charismatically Crafted By Redzwinger #