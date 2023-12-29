"""
Calculates the total size of all txt files in a directory
"""
import os

def file_info():
    total = 0
    # iterate through folders in directory
    for file in os.listdir("deps"):
        # Store path
        path = "deps/" + file
        # Check if it is a file and if it is a txt file
        if os.path.isfile(path) and file.endswith(".txt"):
            total += os.path.getsize(path) # Add to total
    return total

print(file_info())