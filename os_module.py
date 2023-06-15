# Using os to do things

import  os
#
# os.system("echo 'Hello world!")

# Make and change directories

# Change a directory

directory = 'test_dir1'

parent_dir = "C:/Users/Venkat"

path = os.path.join(parent_dir, directory)

# Create Directory

# os.mkdir(path)

# Putting a new file in the new directory

filename = "testfile.txt"
filepath = os.path.join(path, filename)

with open(filepath, "w") as file1:
    tofile = "Contents of the file is written here"
    file1.write(tofile)

print("File " + filename + " created in " + directory + " folder")

