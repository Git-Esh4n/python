# Import the os module to work with directories
import os

# Ask the user to enter the directory path
directory = input("Enter the directory path: ")

try:
    # Display a heading
    print("\nContents of the directory:")

    # Loop through each file and folder in the directory
    for item in os.listdir(directory):
        print(item)

# Handle the case when the directory does not exist
except FileNotFoundError:
    print("Directory not found.")

# Handle the case when permission to access the directory is denied
except PermissionError:
    print("Permission denied.")