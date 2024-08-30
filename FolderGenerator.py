# Import the os module, which contains functions for interacting with the operating system
import os

# Define the names of the folders that you want to create
folder_names = ['Case and Data Files', 'Saved Files', 'Pictures', 'Mesh Files', 'CAD Files', 'Output Files']
#directory = input("Enter the directory location: ")
directory_path = '/Volumes/Drive/Script_Test_Folder'

#if not os.path.isdir(directory):
    #print("Error: The directory does not exist or is not accessible.")
#else:
    #directory_path = directory

# Define the path to the directory where you want to create the folders
# Replace 'example_directory' with the actual directory path
# Create the folders
# for folder_name in folder_names:
#     # Use the os.makedirs() function to create the folders
#     # This function will create any necessary intermediate directories
os.makedirs(os.path.join(directory_path, folder_names))
