
import os
import shutil

def copy_matching_folders(source_dir, compare_dir, destination_dir):
    """
    Copies folders from the source directory to the destination directory if a folder with the same name exists in the compare directory.

    :param source_dir: The directory to search for folders.
    :param compare_dir: The directory to check for matching folder names.
    :param destination_dir: The directory to copy the matching folders to.
    """
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Get the list of folder names in the compare directory
    compare_folders = {folder_name for folder_name in os.listdir(compare_dir) if os.path.isdir(os.path.join(compare_dir, folder_name))}

    # Iterate through the folders in the source directory
    for folder_name in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, folder_name)

        # Check if it is a directory and exists in the compare directory
        if os.path.isdir(folder_path) and folder_name in compare_folders:
            # Copy the folder to the destination directory
            shutil.copytree(folder_path, os.path.join(destination_dir, folder_name))
            print(f"Copied: {folder_name}")

if __name__ == "__main__":
    # Define directories
    source_directory = r"E:\Steam\steamapps\common\assettocorsa\content\tracks\NO\Track Previews\Reboot Project"  # Replace with the path to your source directory
    compare_directory = r"E:\Steam\steamapps\common\assettocorsa\content\tracks"  # Replace with the path to your compare directory
    destination_directory = r"E:\Steam\steamapps\common\assettocorsa\content\tracks\NO\yay"  # Replace with the path to your destination directory

    # Run the folder matching and copying function
    copy_matching_folders(source_directory, compare_directory, destination_directory)
