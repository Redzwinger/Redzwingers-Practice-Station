
import os
import shutil

def move_folders_with_only_ui(source_dir, destination_dir):
    """
    Moves folders containing only a 'ui' subfolder to the destination directory.

    :param source_dir: The directory to search for folders.
    :param destination_dir: The directory to move the matching folders.
    """
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Iterate through the folders in the source directory
    for folder_name in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, folder_name)

        # Check if it is a directory
        if os.path.isdir(folder_path):
            # List the contents of the folder
            subfolders = [item for item in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, item))]

            # Check if the folder contains only a 'ui' subfolder
            if len(subfolders) == 1 and subfolders[0] == "ui":
                # Move the folder to the destination directory
                shutil.move(folder_path, os.path.join(destination_dir, folder_name))
                print(f"Moved: {folder_name}")

if __name__ == "__main__":
    # Define source and destination directories
    source_directory = r"E:\Steam\steamapps\common\assettocorsa\content\tracks"  # Replace with the path to your source directory
    destination_directory = r"E:\Steam\steamapps\common\assettocorsa\content\tracks\NO"  # Replace with the path to your destination directory

    # Run the folder separation function
    move_folders_with_only_ui(source_directory, destination_directory)